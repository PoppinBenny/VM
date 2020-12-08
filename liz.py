from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

lec=[35801,35802]
disc=[47451,35808,53113,51927,35812,35828,53114,35955]
lab=[60732,36010,36017,36022,36030,60731]
#lecture TR12-1

def func1():
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
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
