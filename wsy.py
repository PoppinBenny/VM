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

def func1():
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
    driver.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys('shuyuan2')
    driver.find_element_by_id("easpass").send_keys("Gwo180912!")
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
    ("//option[@value='120191']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//option[@value='ECON']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//tbody/tr[27]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    while True:
        if switch%4==0:
            driver.implicitly_wait(2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='69371 120191']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 13 yet, trying again....')
                    switch+=1
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.find_element_by_link_text("I Agree to the Above Statement").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_name("p_term").find_element_by_xpath\
                    ("//option[@value='120191']").click()
                    driver.find_element_by_xpath("//input[@value='Submit']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//option[@value='SOCW']").click()
                    driver.find_element_by_xpath("//input[@value='Course Search']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//tbody/tr[8]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==1:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='58396 120191']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id4']/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[8]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='58396 120191']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 13 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==2:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='52693 120191']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id4']/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[8]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='52693 120191']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 13 yet, trying again....')
                    switch+=1
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.find_element_by_link_text("I Agree to the Above Statement").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_name("p_term").find_element_by_xpath\
                    ("//option[@value='120191']").click()
                    driver.find_element_by_xpath("//input[@value='Submit']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//option[@value='REL']").click()
                    driver.find_element_by_xpath("//input[@value='Course Search']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//tbody/tr[6]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==3:
            driver.implicitly_wait(2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='68465 120191']")
                shit1.click()
                break
            except NoSuchElementException:
                try:
                    print('no 13 yet, trying again....')
                    switch+=1
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.find_element_by_link_text("I Agree to the Above Statement").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_name("p_term").find_element_by_xpath\
                    ("//option[@value='120191']").click()
                    driver.find_element_by_xpath("//input[@value='Submit']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//option[@value='BTW']").click()
                    driver.find_element_by_xpath("//input[@value='Course Search']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//tbody/tr[3]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()


func1()

print('Course selected')
