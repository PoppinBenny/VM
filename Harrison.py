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

    driver.find_element_by_id("netid").send_keys('lidingl2')
    driver.find_element_by_id("easpass").send_keys('Lld@0217')
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
    driver.find_element_by_xpath("//option[@value='CS']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//tbody/tr[13]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    while True:
        if switch%7==0:
            driver.implicitly_wait(4.8)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='61689 120191']")
                shit2=driver.find_element_by_xpath("//input[@value='61691 120191']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('12')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%7==1:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='61689 120191']")
                shit2=driver.find_element_by_xpath("//input[@value='61692 120191']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('12')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%7==2:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='61689 120191']")
                shit2=driver.find_element_by_xpath("//input[@value='61695 120191']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('12')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%7==3:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='61689 120191']")
                shit2=driver.find_element_by_xpath("//input[@value='61696 120191']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('12')
                    switch+=1
                    driver.back()
                    driver.find_element_by_xpath("//tbody/tr[19]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%7==4:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='65088 120191']")
                shit2=driver.find_element_by_xpath("//input[@value='65089 120191']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('12')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%7==5:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='65088 120191']")
                shit2=driver.find_element_by_xpath("//input[@value='65090 120191']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('12')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%7==6:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='65088 120191']")
                shit2=driver.find_element_by_xpath("//input[@value='65096 120191']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('12')
                    switch+=1
                    driver.back()
                    driver.find_element_by_xpath("//tbody/tr[13]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()

func1()

print('Course selected')
