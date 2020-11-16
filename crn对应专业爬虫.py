import datetime
import os
import sys
import time
import pytz
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

gce = 0
semester_number = '120208'
# 账号密码
account = 'kwang54'
password = 'WOxihuan11'
data = {}

# 是否在gce上面run
if gce == 1:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
else:
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")


def main():
    """主程序"""
    driver.get(
        'https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0-4028-b49f'
        '-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ'
        '%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM-HTTPS'
        '%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu%2euillinois'
        '%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys(account)
    driver.find_element_by_id("easpass").send_keys(password)
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("Registration & Records").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Classic Registration").click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("Look-up or Select Classes").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("I Agree to the Above Statement").click()
    driver.implicitly_wait(10)
    driver.find_element_by_name("p_term").find_element_by_xpath \
        ("//option[@value='" + semester_number + "']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)

    with open('Fall2020 crn数据.json') as fp:
        data = json.load(fp)

    with open('Fall2020 crn数据.json', 'w') as fp:
        major_count = 153
        while True: # major
            try:
                driver.find_element_by_xpath("// *[ @ id = 'subj_id'] / option[" + str(major_count) + "]").click()
                driver.find_element_by_xpath("//input[@value='Course Search']").click()
                driver.implicitly_wait(10)
                xuhao_count = 3
                if major_count==153:
                    xuhao_count=22
                while True: #xuhao
                    try:
                        driver.find_element_by_xpath(
                            "//tbody/tr[" + str(xuhao_count) + "]/td/form/input[@value='View Sections']").click()
                        driver.implicitly_wait(10)
                        xuhao_count+=1
                        crn_count = 3
                        while True: #crn
                            try:
                                crn = driver.find_element_by_xpath(
                                    "/html/body/div[3]/form/table/tbody/tr[" + str(crn_count) + "]/td[2]/a").text
                                major = driver.find_element_by_xpath(
                                    "/html/body/div[3]/form/table/tbody/tr[" + str(crn_count) + "]/td[3]").text
                                xuhao = driver.find_element_by_xpath(
                                    "/html/body/div[3]/form/table/tbody/tr[" + str(crn_count) + "]/td[4]").text
                                data[crn]=major+' '+xuhao
                                print(crn,major,xuhao)
                                crn_count+=1
                            except NoSuchElementException: # no more crn
                                driver.back()
                                break
                    except NoSuchElementException: # no more xuhao
                        driver.back()
                        driver.back()
                        driver.back()
                        major_count += 1
                        driver.find_element_by_link_text("I Agree to the Above Statement").click()
                        driver.implicitly_wait(10)
                        driver.find_element_by_name("p_term").find_element_by_xpath \
                            ("//option[@value='" + semester_number + "']").click()
                        driver.find_element_by_xpath("//input[@value='Submit']").click()
                        driver.implicitly_wait(10)
                        break
            except NoSuchElementException: # no more major
                json.dump(data, fp)
                driver.quit()
                break


main()
print('finish')