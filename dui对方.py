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

major = ['STAT']  # 专业
xuhao = ['430']  # 序号
crn = ['46976']
drops = ['']  # 要drop的crn
xuhao_position = [0] * len(xuhao)  # 序号在页面上的位置
semester_number = '120208'  # 学期序列号

# 计数器
register = 0
limit = 5  # 1.失败register的次数上限
print_counter = 5 * 10
print_counter_limit = print_counter # 2.n分钟*10*6秒之后报告一次还在运行
crn_counter = 0  # 3.下一个crn的计数器
xuhao_counter = 0  # 4.下一个序号的计数器
major_counter = 0  # 5.下一个专业的计数器

# 账号密码
account = 'yuxifan2'
password = '19980706fanxI.'

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
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
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


def next_crn(change_section=False, change_major=False):
    """检测下一个crn"""
    global print_counter
    global crn_counter
    global xuhao_counter
    global xuhao_position
    global major_counter

    print_counter += 1
    crn_counter += 1
    crn_counter = crn_counter % (len(crn))
    if print_counter >= print_counter_limit:
        print_counter = 0
        print('no ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
              datetime.datetime.now(pytz.timezone('Asia/Shanghai')))

    if crn_counter == 0:
        time.sleep(6)

    if change_section:
        driver.back()
        if change_major:
            major_counter += 1
            major_counter = major_counter % len(major)
            driver.back()
            driver.back()
            driver.back()
            driver.find_element_by_link_text("I Agree to the Above Statement").click()
            driver.implicitly_wait(10)
            driver.find_element_by_name("p_term").find_element_by_xpath \
                ("//option[@value='" + semester_number + "']").click()
            driver.find_element_by_xpath("//input[@value='Submit']").click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//option[@value='" + major[major_counter] + "']").click()
            driver.find_element_by_xpath("//input[@value='Course Search']").click()
            driver.implicitly_wait(10)
        xuhao_counter += 1
        xuhao_counter = xuhao_counter % len(xuhao)
        if xuhao_position[xuhao_counter] == 0:
            xuhao_position[xuhao_counter] = find(xuhao[xuhao_counter])
        driver.find_element_by_xpath(
            "//tbody/tr[" + str(xuhao_position[xuhao_counter]) + "]/td/form/input[@value='View Sections']").click()


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


def normal(crn):
    """正常选"""
    global register
    shit1 = driver.find_element_by_xpath("//input[@value='" + crn + " " + semester_number + "']")
    shit1.click()
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)
    i = 2
    try:
        while True:
            number = driver.find_element_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[3]").text
            c = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[4]").text
            nu = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[5]").text
            print(c, nu, number)
            if crn == number:
                print('Course selected')
                driver.quit()
            i += 1
    except NoSuchElementException:
        print('Failed to add ' + crn + ' ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
              datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
        print_error()
        register += 1
        if register >= limit:
            print('Too many requests for ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
                  datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
            driver.quit()
        driver.back()
    raise NoSuchElementException


def drop_mode(crn, drop):
    """drop模式"""
    global register
    shit1 = driver.find_element_by_xpath("//input[@value='" + crn + " " + semester_number + "']")
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)
    find_drop(drop)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_id("crn_id1").send_keys(crn)
    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
    driver.implicitly_wait(10)
    i = 2
    try:
        while True:
            number = driver.find_element_by_xpath(
                "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[3]").text
            c = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[4]").text
            nu = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[5]").text
            print(c, nu, number)
            if crn == number:
                print('Course selected')
                driver.quit()
            i += 1
    except NoSuchElementException:
        print('Failed to add ' + crn + ' ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
              datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
        print_error()
        driver.find_element_by_id("crn_id1").send_keys(drop)
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
    if new_login:
        driver.get('https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0'
                   '-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ'
                   '%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM'
                   '-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu'
                   '%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1 ')
        driver.implicitly_wait(7.5)
        driver.find_element_by_id("netid").send_keys(account)
        driver.find_element_by_id("easpass").send_keys(password)
        #driver.find_element_by_name("BTN_LOGIN").click()
        driver.implicitly_wait(10)
    if not new_login:
        driver.get('https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu')

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

    if len(drops) == 0:
        try:
            i = 2
            repeat = False
            while True:
                c = driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[4]").text
                nu = driver.find_element_by_xpath(
                    "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[5]").text
                for m in major:
                    if repeat:
                        break
                    for x in xuhao:
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

    if len(drops) != 0:
        for drop in drops:
            i = 2
            try:
                while True:
                    temp = driver.find_element_by_xpath(
                        "//html/body/div[3]/form/table[1]/tbody/tr[" + str(i) + "]/td[3]").text
                    if drop == temp:
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
    driver.find_element_by_xpath("//option[@value='" + major[0] + "']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    xuhao_position[0] = find(xuhao[0])
    driver.find_element_by_xpath(
        "//tbody/tr[" + str(xuhao_position[0]) + "]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10)  # 440 = 36, 412 = 24

    while True:
        try:
            driver.implicitly_wait(0.2)
            if len(drops) == 0:
                normal(crn[crn_counter])
            else:
                drop_mode(crn[crn_counter], drops[0])
            break
        except NoSuchElementException:
            try:
                next_crn(True)
            except NoSuchElementException:
                time.sleep(30)
                driver.close()
                main()


main()

print('Course selected')
