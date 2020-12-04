import datetime
import os
import sys
import time
import pytz
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

gce = 1

# 打开crn数据库
with open('Spring2021 crn数据.json') as fp:
    data = json.load(fp)

crn = [70358]
crn_together = {
    # crn[]: [],
}  # 一个crn可能有的lab和discussion
drops = {
    crn[0]: [63552],
}  # 要选的crn对应要drop的crn
xuhao_position = {}  # 序号在页面上的位置
semester_number = '120211'  # 学期序列号

# 账号密码
account = 'jingx7'
password = '135135Xj'

# 计数器
register = 0
limit = 5  # 1.失败register的次数上限
print_counter = 5 * 10
print_counter_limit = print_counter  # 2.n分钟*10*6秒之后报告一次还在运行
crn_counter = 0  # 3.下一个crn的计数器
previous_course = ''

driver_data = {}
# 是否在gce上面run
with open('urlid.json', 'r') as fp2:
    driver_data = json.load(fp2)

file = os.path.basename(sys.argv[0])
new_login = file not in driver_data
with open('urlid.json', 'w') as fp2:
    if new_login:
        if gce == 1:
            options = Options()
            #options.add_argument('--headless')
            #options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
        else:
            driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driver_data[file] = [driver.command_executor._url, driver.session_id]
    else:
        driver = webdriver.Remote(command_executor=driver_data[file][0],
                                  desired_capabilities={})
        driver.session_id = driver_data[file][1]
    json.dump(driver_data, fp2)

print(driver.command_executor._url, driver.session_id)


def find_drop(index):
    """找到要drop的crn并drop"""
    i = 2
    try:
        while True:
            number = driver.find_element_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[3]").text
            if str(index) == number:
                driver.find_element_by_xpath("//*[@id='action_id" + str(i - 1) + "']/option[2]").click()
                break
            i += 1
    except NoSuchElementException:
        print('Drop index does not exist')
        driver.quit()


def find(A):
    """找到序号在页面上的位置"""
    i = 3
    try:
        while True:
            number = driver.find_element_by_xpath("//html/body/div[3]/table[2]/tbody/tr[" + str(i) + "]/td[1]").text
            if A == number:
                break
            i += 1
    except NoSuchElementException:
        print('Course index does not exist')
        driver.quit()

    return i


def next_crn():
    """检测下一个crn"""
    global print_counter
    global crn_counter
    global xuhao_position
    global previous_course

    if print_counter >= print_counter_limit:
        print_counter = 0
        print('no ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
              datetime.datetime.now(pytz.timezone('Asia/Shanghai')))

    crn_counter += 1
    crn_counter = crn_counter % (len(crn))

    course = data[str(crn[crn_counter])]
    major = course.split()[0]
    xuhao = course.split()[1]
    # 当下一个crn的课不同，或crn遍历一遍之后，需要退出去重新找section
    if previous_course != course or crn_counter == 0:
        print_counter += 1
        time.sleep(6.0 / (len(xuhao_position.values())))
        driver.back()
        previous_major = previous_course.split()[0]
        if previous_major != major:
            driver.back()
            driver.back()
            driver.back()
            driver.find_element_by_link_text("I Agree to the Above Statement").click()
            driver.implicitly_wait(10)
            driver.find_element_by_name("p_term").find_element_by_xpath(
                "//option[@value='" + semester_number + "']").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//option[@value='" + major + "']").click()
            driver.find_element_by_xpath("//input[@value='Course Search']").click()
            driver.implicitly_wait(10)
        if course not in xuhao_position:  # 如果现在crn的课还不知道在页面上位置
            xuhao_position[course] = find(xuhao)
        driver.find_element_by_xpath(
            "//tbody/tr[" + str(xuhao_position[course]) + "]/td/form/input[@value='View Sections']").click()
        if 'error' in driver.current_url:
            print(os.path.basename(sys.argv[0]), 'banner self-service error')
    previous_course = course


def print_error():
    """print没选上课的error"""
    i = 2
    try:
        while True:
            status = driver.find_element_by_xpath("/html/body/div[3]/form/table[4]/tbody/tr[" + str(i) + "]/td[1]").text
            c = driver.find_element_by_xpath("/html/body/div[3]/form/table[4]/tbody/tr[" + str(i) + "]/td[2]").text
            print(c, status)
            i += 1
    except NoSuchElementException:
        print('try again')


def select(target_crn, drop=None):
    """选课并确认是否选上"""
    global register
    if drop is None:
        drop = []
    # 搜所有目标crn
    shit = driver.find_element_by_xpath("//input[@value='" + str(target_crn) + " " + semester_number + "']")
    target_crns = [str(target_crn)]  # 存一下本循环需要的所有crn
    target_elements = [shit]  # 存一下crn对应的网页元素
    if target_crn in crn_together:
        for together in crn_together[target_crn]:
            shit = driver.find_element_by_xpath("//input[@value='" + str(together) + " " + semester_number + "']")
            target_elements.append(shit)
            target_crns.append(str(together))
    target_crn = str(target_crn)
    print(os.path.basename(sys.argv[0]), 'found', target_crn)

    # 如果没有drop则挨个click直接选课
    if not drop:
        for e in target_elements:
            e.click()
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)

    # 如果有drop
    if drop:
        # drop课
        for i in range(len(drop)):
            find_drop(str(drop[i]))
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
        driver.implicitly_wait(10)
        # 注册目标crn
        for i in range(len(target_crns)):
            driver.find_element_by_id("crn_id" + str(i + 1)).send_keys(target_crns[i])
        driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
        driver.implicitly_wait(10)

    # 复查目标crn是否选上
    i = 2
    try:
        while True:
            number = driver.find_element_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[3]").text
            c = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[4]").text
            nu = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[5]").text
            print(c, nu, number)  # 打课表
            if target_crn == number:
                print('Time in Chicago, IL, USA:', datetime.datetime.now(pytz.timezone('America/Chicago')))
                print('Course selected')
                driver.quit()
            i += 1
    except NoSuchElementException:
        print('Failed to add ' + target_crn + ' ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
              datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
        print_error()
        register += 1
        if register >= limit:
            print('Too many requests for ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
                  datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
            driver.quit()
        # 如果有drop，但是没选上，加回一开始drop的crn
        if drop:
            for i in range(len(drop)):
                driver.find_element_by_id("crn_id" + str(i + 1)).send_keys(str(drop[i]))
            driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
            driver.back()
            driver.back()
            driver.back()
        driver.back()
    raise NoSuchElementException


def main():
    """主程序"""
    global previous_course
    global new_login
    if new_login:
        if gce == 1:
            driver.get('https://banner.apps.uillinois.edu/StudentRegistrationSSB/ssb/registration?mepCode=1UIUC')
            driver.find_element_by_xpath("//*[@id='registerLink']/span[1]").click()
            driver.implicitly_wait(10)
            driver.find_element_by_id("netid").send_keys(account)
            driver.find_element_by_id("easpass").send_keys(password)
            driver.find_element_by_name("BTN_LOGIN").click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//*[@id='s2id_txt_term']/a/span[2]/b").click()
            time.sleep(2)
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//*[@id='" + semester_number + "']").click()
            driver.find_element_by_xpath("//*[@id='term-go']").click()
            time.sleep(5)
            try:
                driver.find_element_by_xpath("//*[@id='check_agreement']").click()
                driver.implicitly_wait(10)
                driver.find_element_by_xpath("/html/body/div[18]/div[11]/div/button").click()
                driver.implicitly_wait(10)
                driver.find_element_by_xpath("//*[@id='notification-center']/div/ul[2]/li/div[2]/button").click()
                driver.implicitly_wait(10)
            except Exception:
                pass
            driver.find_element_by_xpath("//*[@id='enterCRNs-tab']").click()
            time.sleep(2)
            driver.implicitly_wait(10)

            for target_crn in crn:
                target_crns = [str(target_crn)]  # 存一下本循环需要的所有crn
                if target_crn in crn_together:
                    for together in crn_together[target_crn]:
                        target_crns.append(str(together))
                if len(target_crns) > 1:
                    for i in range(len(target_crns) - 1):
                        driver.find_element_by_xpath("//*[@id='addAnotherCRN']").click()
                for i in range(len(target_crns)):
                    driver.find_element_by_xpath("//*[@id='txt_crn" + str(i + 1) + "']").send_keys(target_crns[i])
                driver.find_element_by_xpath("//*[@id='addCRNbutton']").click()
                time.sleep(1)
                driver.implicitly_wait(10)
                driver.find_element_by_xpath("//*[@id='saveButton']").click()
                driver.implicitly_wait(10)
                elements = driver.find_elements_by_class_name("notification-flyout-item")
                for elem in elements:
                    err = elem.text
                    if ("Closed Section" not in err) and ("Linked course required" not in err) \
                            and (len(target_crns) <= 1):
                        print(err)
                driver.find_element_by_xpath("//*[@id='saveButton']").click()
                time.sleep(3)
        driver.get('https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0'
                   '-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ'
                   '%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM'
                   '-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu'
                   '%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1')
        try:
            driver.switch_to.alert.accept()
        except Exception:
            pass
        driver.implicitly_wait(7.5)
        driver.find_element_by_id("netid").send_keys(account)
        driver.find_element_by_id("easpass").send_keys(password)
        driver.find_element_by_name("BTN_LOGIN").click()
        driver.implicitly_wait(10)
    if not new_login:
        driver.get('https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu')
        time.sleep(5)
        driver.implicitly_wait(10)

    try:
        driver.find_element_by_link_text("Registration & Records").click()
    except Exception:
        print(os.path.basename(sys.argv[0]), 'Did not find registration button')
        time.sleep(30)
        if not new_login:
            main()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Classic Registration").click()
    driver.implicitly_wait(10)
    if new_login:
        driver.find_element_by_link_text("Add/Drop Classes").click()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text("I Agree to the Above Statement").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='term_id']/option[1]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.implicitly_wait(10)

        current = int(float(driver.find_element_by_xpath("/html/body/div[3]/form/\
                table[2]/tbody/tr[1]/td[2]").text))
        maximum = int(float(driver.find_element_by_xpath("/html/body/div[3]/form/table\
                [2]/tbody/tr[4]/td[2]").text))
        if maximum - current < 3 and len(drops.values()) == 0:
            print(os.path.basename(sys.argv[0]), "has insufficient credits. Current:", current, "Maximum:", maximum)
            driver.quit()
        # 如果没有drop的课,检查重复的课
        if len(drops.values()) == 0:
            cs = driver.find_elements_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr/td[4]")
            nus = driver.find_elements_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr/td[5]")
            temp = []
            for i in range(len(cs)):
                temp.append(cs[i].text + ' ' + nus[i].text)
            want_courses = [data[str(cr)] for cr in crn]
            if any(elem in temp for elem in want_courses):
                print(temp, want_courses)
                print('Repeated courses')
                driver.quit()

        # 如果有drop的课,检查是否在在课表内
        if len(drops.values()) != 0:
            temp = driver.find_elements_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr/td[3]")
            d = [str(drop[0]) for drop in drops.values()]
            c = [t.text for t in temp]
            if not all(elem in c for elem in d):
                print(d, c)
                print('Drop index does not exist')
                driver.quit()
        driver.back()
        driver.back()
        driver.back()
        new_login = False

    driver.find_element_by_link_text("Look-up or Select Classes").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("I Agree to the Above Statement").click()
    driver.implicitly_wait(10)
    driver.find_element_by_name("p_term").find_element_by_xpath(
        "//option[@value='" + semester_number + "']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)

    course = data[str(crn[crn_counter])]
    previous_course = course
    m = course.split()[0]
    c = course.split()[1]
    driver.find_element_by_xpath("//option[@value='" + m + "']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)
    xuhao_position[course] = find(c)
    driver.find_element_by_xpath(
        "//tbody/tr[" + str(xuhao_position[course]) + "]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10)  # 440 = 36, 412 = 24

    while True:
        try:
            driver.implicitly_wait(0.2)
            target = crn[crn_counter]
            if target not in drops:
                select(target)
            else:
                select(target, drops[target])
            break
        except NoSuchElementException:
            try:
                next_crn()
            except Exception as e:
                print(e)
                time.sleep(30)
                main()


main()

print('Course selected')
