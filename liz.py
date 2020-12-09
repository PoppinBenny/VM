import datetime
import os
import sys
import time
import pytz
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')

lec=[35801,35802]
disc=[47451,35808,53113,51927,35812,35828,53114,35955]
lab=[60732,36010,36017,36022,36030,60731]
#lecture TR12-1

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

def func1():
    driver.get('https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0'
               '-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ'
               '%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM'
               '-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu'
               '%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1')
    driver.implicitly_wait(7.5)
    driver.find_element_by_id("netid").send_keys('zeyuli5')
    driver.find_element_by_id("easpass").send_keys('Lizeyu010705bill')
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
    driver.find_element_by_name("p_term").find_element_by_xpath\
    ("//option[@value='120211']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//option[@value='PHYS']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//tbody/tr[6]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    b=False
    register=0
    while True:
        print('no liz')
        for i in lec:
            for j in disc:
                for k in lab:
                    driver.implicitly_wait(0.25)
                    try:
                        str1="//input[@value='"+str(i)+" 120211']"
                        str2="//input[@value='"+str(j)+" 120211']"
                        str3="//input[@value='"+str(k)+" 120211']"
                        shit1=driver.find_element_by_xpath(str1)
                        shit2=driver.find_element_by_xpath(str2)
                        shit3=driver.find_element_by_xpath(str3)
                        shit1.click()
                        shit2.click()
                        shit3.click()
                        driver.find_element_by_xpath("//input[@value='Register']").click()
                        b=True
                        driver.implicitly_wait(7.5)

                        # 复查目标crn是否选上
                        x = 2
                        try:
                            while True:
                                number = driver.find_element_by_xpath(
                                    "//html/body/div[3]/form/table[1]/tbody/tr[" + str(x) + "]/td[3]").text
                                c = driver.find_element_by_xpath(
                                    "//html/body/div[3]/form/table[1]/tbody/tr[" + str(x) + "]/td[4]").text
                                nu = driver.find_element_by_xpath(
                                    "//html/body/div[3]/form/table[1]/tbody/tr[" + str(x) + "]/td[5]").text
                                print(c, nu, number)  # 打课表
                                if str(i) == number:
                                    print('Time in Chicago, IL, USA:',
                                          datetime.datetime.now(pytz.timezone('America/Chicago')))
                                    print('Course selected')
                                    driver.quit()
                                x += 1
                        except NoSuchElementException:
                            print('Failed to add ' + str(i) + ' ' + os.path.basename(
                                sys.argv[0]) + ', ' + 'Time in China: ',
                                  datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
                            print_error()
                            register += 1
                            if register >= 5:
                                print(
                                    'Too many requests for ' + os.path.basename(sys.argv[0]) + ', ' + 'Time in China: ',
                                    datetime.datetime.now(pytz.timezone('Asia/Shanghai')))
                                driver.quit()
                            driver.back()
                    except NoSuchElementException:
                        try:
                            switch+=1
                            if switch==len(lec)*len(disc)*len(lab):
                                switch=0
                                driver.back()
                                driver.find_element_by_xpath("//tbody/tr[6]/td/form/input[@value='View Sections']").click()
                        except NoSuchElementException:
                            time.sleep(30)
                            driver.close()
                            func1()
        if b==True:
            break


func1()

print('Course selected')
