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
    driver.implicitly_wait(5)

    driver.find_element_by_id("netid").send_keys('yinhu2')
    driver.find_element_by_id("easpass").send_keys('hmh21HMH05')
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
    driver.find_element_by_id("term_input_id").find_element_by_xpath\
    ("//option[@value='120188']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//option[@value='STAT']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    while True:
        if switch%6==0:
            driver.implicitly_wait(1)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='45556 120188']")
                shit2=driver.find_element_by_xpath("//input[@value='49241 120188']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id6']/option[@value='DW']").click()
                driver.find_element_by_xpath("//*[@id='action_id7']/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='45556 120188']").click()
                driver.find_element_by_xpath("//input[@value='49241 120188']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no available yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%6==1:
            driver.implicitly_wait(1)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='45556 120188']")
                shit2=driver.find_element_by_xpath("//input[@value='65036 120188']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id6']/option[@value='DW']").click()
                driver.find_element_by_xpath("//*[@id='action_id7']/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='45556 120188']").click()
                driver.find_element_by_xpath("//input[@value='65036 120188']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no available yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%6==2:
            driver.implicitly_wait(1)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='45556 120188']")
                shit2=driver.find_element_by_xpath("//input[@value='65038 120188']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id6']/option[@value='DW']").click()
                driver.find_element_by_xpath("//*[@id='action_id7']/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='45556 120188']").click()
                driver.find_element_by_xpath("//input[@value='65038 120188']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no available yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%6==3:
            driver.implicitly_wait(1)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='35005 120188']")
                shit2=driver.find_element_by_xpath("//input[@value='65038 120188']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id6']/option[@value='DW']").click()
                driver.find_element_by_xpath("//*[@id='action_id7']/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='35005 120188']").click()
                driver.find_element_by_xpath("//input[@value='65038 120188']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no available yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%6==4:
            driver.implicitly_wait(1)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='35005 120188']")
                shit2=driver.find_element_by_xpath("//input[@value='65038 120188']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id6']/option[@value='DW']").click()
                driver.find_element_by_xpath("//*[@id='action_id7']/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='35005 120188']").click()
                driver.find_element_by_xpath("//input[@value='65038 120188']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no available yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%6==5:
            driver.implicitly_wait(1)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='35005 120188']")
                shit2=driver.find_element_by_xpath("//input[@value='65038 120188']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                driver.find_element_by_xpath("//*[@id='action_id6']/option[@value='DW']").click()
                driver.find_element_by_xpath("//*[@id='action_id7]/option[@value='DW']").click()
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(7.5)
                driver.back()
                driver.back()
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
                driver.find_element_by_xpath("//input[@value='35005 120188']").click()
                driver.find_element_by_xpath("//input[@value='65038 120188']").click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no available yet, trying again....')
                    switch+=1
                    driver.back()
                    driver.implicitly_wait(30)
                    driver.find_element_by_xpath("//tbody/tr[10]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        

func1()

print('Course selected')


