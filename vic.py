from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

gce=True
major='STAT'
xuhao1='430'
crn1='69110'

if gce:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
else:
    driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")


def find_drop(index):
    i=2
    try:
        while True:
            number=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[3]").text
            if str(index)==number:
                driver.find_element_by_xpath("//*[@id='action_id"+str(i-1)+"']/option[@value='DW']").click()
                break
            i+=1
    except NoSuchElementException:
        print('Index does not exist')
        driver.quit()

def find(A):
    i=3
    try:
        while True:
            number=driver.find_element_by_xpath("//html/body/div[3]/table[2]/tbody/tr["+str(i)+"]/td[1]").text
            if A==number:
                break
            i+=1
    except NoSuchElementException:
        print('Index does not exist')
        driver.quit()
        
    return i


def func1():
    driver.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys('xinsui2')
    driver.find_element_by_id("easpass").send_keys("SXq1w2e3")
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)

    driver.find_element_by_id("netid").send_keys('xinsui2')
    driver.find_element_by_id("easpass").send_keys("SXq1w2e3")
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
    ("//option[@value='120201']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//option[@value='"+major+"']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    i1=find(xuhao1)
    driver.find_element_by_xpath("//tbody/tr["+str(i1)+"]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    while True:
        if switch%5==0:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='"+crn1+" 120201']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 6')
                    switch+=1
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.find_element_by_link_text("I Agree to the Above Statement").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_name("p_term").find_element_by_xpath\
                    ("//option[@value='120201']").click()
                    driver.find_element_by_xpath("//input[@value='Submit']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//option[@value='DANC']").click()
                    driver.find_element_by_xpath("//input[@value='Course Search']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//tbody/tr[3]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%5==1:
            driver.implicitly_wait(3)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='63899 120201']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    switch+=1                    
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%5==2:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='63899 120201']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    switch+=1                    
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%5==3:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='63899 120201']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    switch+=1                    
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%5==4:
            driver.implicitly_wait(0.2)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='63899 120201']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    switch+=1
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.find_element_by_link_text("I Agree to the Above Statement").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_name("p_term").find_element_by_xpath\
                    ("//option[@value='120201']").click()
                    driver.find_element_by_xpath("//input[@value='Submit']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//option[@value='STAT']").click()
                    driver.find_element_by_xpath("//input[@value='Course Search']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//tbody/tr["+i1+"]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()


func1()

print('Course selected')
