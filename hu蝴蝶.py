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
with open('Fall2020 crn数据.json') as fp:
    data = json.load(fp)

crn = [65613,58798,62207,63341]
crn_together = {
    # crn[]: [],
}  # 一个crn可能有的lab和discussion
drops = {
    crn[0]: [63856],
    crn[1]: [63856],
    crn[2]: [63856],
    crn[3]: [63856],
}  # 要选的crn对应要drop的crn
xuhao_position = {}  # 序号在页面上的位置
semester_number = '120208'  # 学期序列号

# 账号密码
account = 'yimingz6'
password = 'Aabb57117513!'

# 计数器
register = 0
limit = 5  # 1.失败register的次数上限
print_counter = 5 * 10
print_counter_limit = print_counter  # 2.n分钟*10*6秒之后报告一次还在运行
crn_counter = 0  # 3.下一个crn的计数器
previous_major = ''
previous_xuhao = ''


# 是否在gce上面run
if gce == 1:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
else:
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")


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
    global previous_major
    global previous_xuhao

    print_counter += 1
    if print_counter >= print_counter_limit:
        print_counter = 0
        print('no ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
              datetime.datetime.now(pytz.timezone('Asia/Shanghai')))

    crn_counter += 1
    crn_counter = crn_counter % (len(crn))

    course = data[str(crn[crn_counter])]
    major = course.split()[0]
    xuhao = course.split()[1]
    if previous_xuhao != xuhao or crn_counter==0:
        driver.back()
        time.sleep(6.0/(len(xuhao_position.values())))
        if previous_major != major:
            driver.back()
            driver.back()
            driver.back()
            driver.find_element_by_link_text("I Agree to the Above Statement").click()
            driver.implicitly_wait(10)
            driver.find_element_by_name("p_term").find_element_by_xpath \
                ("//option[@value='" + semester_number + "']").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//option[@value='" + major + "']").click()
            driver.find_element_by_xpath("//input[@value='Course Search']").click()
            driver.implicitly_wait(10)
        if course not in xuhao_position:  # 如果现在crn的课还不知道在页面上位置
            xuhao_position[course] = find(xuhao)
        driver.find_element_by_xpath(
            "//tbody/tr[" + str(xuhao_position[course]) + "]/td/form/input[@value='View Sections']").click()
    previous_major = major
    previous_xuhao = xuhao


def print_error():
    """print没选上课的error"""
    i = 2
    try:
        while True:
            status = driver.find_element_by_xpath("/html/body/div[3]/form/table[4]/tbody/tr[" + str(i) + "]/td[1]").text
            crn = driver.find_element_by_xpath("/html/body/div[3]/form/table[4]/tbody/tr[" + str(i) + "]/td[2]").text
            print(crn, status)
            i += 1
    except NoSuchElementException:
        print('try again')


def normal(target_crn):
    """正常选"""
    global register
    # 搜所有目标crn
    target_crn = str(target_crn)
    shit = driver.find_element_by_xpath("//input[@value='" + target_crn + " " + semester_number + "']")
    target_elements = [shit]
    if target_crn in crn_together:
        for together in crn_together[target_crn]:
            shit = driver.find_element_by_xpath("//input[@value='" + str(together) + " " + semester_number + "']")
            target_elements.append(shit)
    print(os.path.basename(sys.argv[0]),'found',target_crn)
    for e in target_elements:
        e.click()
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)
    # 复查目标crn是否选上
    i = 2
    try:
        while True:
            number = driver.find_element_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[3]").text
            c = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[4]").text
            nu = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[5]").text
            print(c, nu, number)
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
        driver.back()
    raise NoSuchElementException


def drop_mode(target_crn, drop):
    """drop模式"""
    global register
    # 搜所有目标crn
    target_crn = str(target_crn)
    shit = driver.find_element_by_xpath("//input[@value='" + target_crn + " " + semester_number + "']")
    target_crns = [target_crn]
    if target_crn in crn_together:
        for together in crn_together[target_crn]:
            shit = driver.find_element_by_xpath("//input[@value='" + str(together) + " " + semester_number + "']")
            target_crns.append(str(together))
    print(os.path.basename(sys.argv[0]), 'found', target_crn)
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)
    # drop课
    for i in range(len(drop)):
        find_drop(str(drop[i]))
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
    driver.implicitly_wait(10)
    # 注册目标crn
    for i in range(len(target_crns)):
        driver.find_element_by_id("crn_id"+str(i+1)).send_keys(target_crns[i])
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
            print(c, nu, number)
            if target_crn == number:
                print('Time in Chicago, IL, USA:', datetime.datetime.now(pytz.timezone('America/Chicago')))
                print('Course selected')
                driver.quit()
            i += 1
    except NoSuchElementException:
        print('Failed to add ' + target_crn + ' ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
              datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
        print_error()
        # 如果没有选上则加回drop掉的crn
        for i in range(len(drop)):
            driver.find_element_by_id("crn_id" + str(i + 1)).send_keys(str(drop[i]))
        driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
        driver.implicitly_wait(10)
        register += 1
        if register >= limit:
            print('Too many requests for ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
                  datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
            driver.quit()
        driver.back()
        driver.back()
        driver.back()
        driver.back()
    raise NoSuchElementException


def main():
    """主程序"""
    driver.get('https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0'
               '-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ'
               '%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM'
               '-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu'
               '%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1 ')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys(account)
    driver.find_element_by_id("easpass").send_keys(password)
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("Registration & Records").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Classic Registration").click()
    driver.implicitly_wait(10)
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
    if maximum - current < 3 and len(drops) == 0:
        print(os.path.basename(sys.argv[0]), "has insufficient credits. Current:", current, "Maximum:", maximum)
        driver.quit()
    # 如果没有drop的课,检查重复的课
    if len(drops.values()) == 0:
        try:
            i = 2
            repeat = False
            while True:
                c = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[4]").text
                nu = driver.find_element_by_xpath(
                    "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[5]").text
                for cr in crn:
                    m = data[str(cr)].split()[0]
                    x = data[str(cr)].split()[1]
                    if repeat:
                        break
                    if m == c and x == nu:
                        repeat = True
                        break
                if repeat:
                    print(c + nu + ' already existed ' + os.path.basename(sys.argv[0]))
                    driver.quit()
                    break
                i += 1
        except NoSuchElementException:
            driver.back()
            driver.back()
            driver.back()
    # 如果有drop的课,检查是否在在课表内
    if len(drops.values()) != 0:
        for drop in drops.values():
            i = 2
            try:
                while True:
                    temp = driver.find_element_by_xpath(
                        "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[3]").text
                    if str(drop[0]) == temp:
                        break
                    i += 1
            except NoSuchElementException:
                print('Drop index does not exist')
                driver.quit()
        driver.back()
        driver.back()
        driver.back()

    driver.find_element_by_link_text("Look-up or Select Classes").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("I Agree to the Above Statement").click()
    driver.implicitly_wait(10)
    driver.find_element_by_name("p_term").find_element_by_xpath \
        ("//option[@value='" + semester_number + "']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    course = data[str(crn[crn_counter])]
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
                normal(target)
            else:
                drop_mode(target, drops[target])
            break
        except NoSuchElementException:
            try:
                next_crn()
            except NoSuchElementException:
                time.sleep(30)
                driver.close()
                main()


main()

print('Course selected')
