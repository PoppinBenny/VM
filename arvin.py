from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

gce=True

major1='STAT'
xuhao1='448'
crn1='67124'
crn11='67126'

xuhao2='440'
crn2='56929'

xuhao3='443'
crn3='70358'

drop1='33998'


account='yipinl2'
password='Yp961227'
n='8'

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
        print('Drop index does not exist')
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
        print('Course index does not exist')
        driver.quit()
        
    return i 


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
    i2=0
    i3=0
    driver.find_element_by_xpath("//tbody/tr["+str(i1)+"]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    while True:
        if switch%4==0:
                driver.implicitly_wait(1.5)
                try:
                    shit1=driver.find_element_by_xpath("//input[@value='"+crn1+" 120201']")
                    driver.find_element_by_xpath("//input[@value='Register']").click()
                    driver.implicitly_wait(7.5)
                    find_drop(drop1)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_id("crn_id1").send_keys(crn1)
                    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                    break
                except NoSuchElementException:
                    try:
                        print('no '+n)
                        switch+=1
                    except NoSuchElementException:
                        time.sleep(30)
                        driver.close()
                        func1()
        if switch%4==1:
                driver.implicitly_wait(1.5)
                try:
                    shit1=driver.find_element_by_xpath("//input[@value='"+crn11+" 120201']")
                    driver.find_element_by_xpath("//input[@value='Register']").click()
                    driver.implicitly_wait(7.5)
                    find_drop(drop1)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_id("crn_id1").send_keys(crn11)
                    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                    break
                except NoSuchElementException:
                    try:
                        switch+=1
                        driver.back()
                        if i2==0:
                            i2=find(xuhao2)
                        driver.find_element_by_xpath("//tbody/tr["+str(i2)+"]/td/form/input[@value='View Sections']").click()
                    except NoSuchElementException:
                        time.sleep(30)
                        driver.close()
                        unc1()
        if switch%4==2:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='"+crn2+" 120201']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                find_drop(drop1)
                driver.implicitly_wait(10)
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(10)
                driver.find_element_by_id("crn_id1").send_keys(crn2)
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                break
            except NoSuchElementException:
                try:
                    switch+=1
                    driver.back()
                    if i3==0:
                        i3=find(xuhao3)
                    driver.find_element_by_xpath("//tbody/tr["+str(i3)+"]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==3:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='"+crn3+" 120201']")
                driver.find_element_by_xpath("//input[@value='Register']").click()
                driver.implicitly_wait(7.5)
                find_drop(drop1)
                driver.implicitly_wait(10)
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                driver.implicitly_wait(10)
                driver.find_element_by_id("crn_id1").send_keys(crn3)
                driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
                break
            except NoSuchElementException:
                try:
                    switch+=1
                    driver.back()
                    driver.find_element_by_xpath("//tbody/tr["+str(i1)+"]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()


func1()

print('Course selected')
