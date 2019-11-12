from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

gce=True

major1='ACCY'
xuhao1='571'
crn=['68538']

drops=[] #要加引号

account='mzhou33'
password='681021Zmymia33zmyzlx'
n='9'

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

def normal(crn):
    shit1=driver.find_element_by_xpath("//input[@value='"+crn+" 120201']")
    shit1.click()
    driver.find_element_by_xpath("//input[@value='Register']").click()

def drop_mode(crn,drop):
    shit1=driver.find_element_by_xpath("//input[@value='"+crn+" 120201']")
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)
    find_drop(drop)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_id("crn_id1").send_keys(crn)
    driver.find_element_by_xpath("//input[@value='Submit Changes']")


def func1():
    driver.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys(account)
    driver.find_element_by_id("easpass").send_keys(password)
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)

    driver.find_element_by_id("netid").send_keys(account)
    driver.find_element_by_id("easpass").send_keys(password)
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("Registration & Records").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Classic Registration").click()
    driver.implicitly_wait(10)

    if len(drops)!=0:
        for drop in drops:
            driver.find_element_by_link_text("Add/Drop Classes").click()
            driver.implicitly_wait(10)
            driver.find_element_by_link_text("I Agree to the Above Statement").click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//input[@value='Submit']").click()
            driver.implicitly_wait(10)
            i=2
            try:
                while True:
                    temp=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[3]").text
                    if drop==temp:
                        driver.back()
                        driver.back()
                        driver.back()
                        break
                    i+=1
            except NoSuchElementException:
                print('Drop index does not exist')
                driver.quit()

    driver.find_element_by_link_text("Look-up or Select Classes").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("I Agree to the Above Statement").click()
    driver.implicitly_wait(10)
    driver.find_element_by_name("p_term").find_element_by_xpath\
    ("//option[@value='120201']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//option[@value='"+major1+"']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    i1=find(xuhao1)
    driver.find_element_by_xpath("//tbody/tr["+str(i1)+"]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    while True:
            driver.implicitly_wait(6)
            try:
                if len(drops)==0:
                    normal(crn[0])
                else:
                    drop_mode(crn[0],drops[0])
                break
            except NoSuchElementException:
                try:
                    print('no '+n)
                    driver.back()
                    driver.find_element_by_xpath("//tbody/tr["+str(i1)+"]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()


func1()

print('Course selected')
