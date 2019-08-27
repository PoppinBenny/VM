from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

gce=True

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


def func1():
    driver.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys('yueniw2')
    driver.find_element_by_id("easpass").send_keys("Wyn990413yz")
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)
    driver.find_element_by_id("netid").send_keys('yueniw2')
    driver.find_element_by_id("easpass").send_keys("Wyn990413yz")
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
    ("//option[@value='120198']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//option[@value='STAT']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//tbody/tr[13]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    while True:
        if switch%4==0:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='65080 120198']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==1:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='58798 120198']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                    driver.back()
                    driver.find_element_by_xpath("//tbody/tr[14]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==2:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='63856 120198']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==3:
            driver.implicitly_wait(1.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='68358 120198']")
                shit1.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                    driver.back()
                    driver.find_element_by_xpath("//tbody/tr[13]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        '''if switch%4==4:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='30102 120198']")
                shit2=driver.find_element_by_xpath("//input[@value='51499 120198']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==5:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='30102 120198']")
                shit2=driver.find_element_by_xpath("//input[@value='63143 120198']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==6:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='30102 120198']")
                shit2=driver.find_element_by_xpath("//input[@value='63145 120198']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==7:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='30102 120198']")
                shit2=driver.find_element_by_xpath("//input[@value='63146 120198']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==8:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='40083 120198']")
                shit2=driver.find_element_by_xpath("//input[@value='71541 120198']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==9:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='40083 120198']")
                shit2=driver.find_element_by_xpath("//input[@value='63147 120198']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()
        if switch%4==10:
            driver.implicitly_wait(0.5)
            try:
                shit1=driver.find_element_by_xpath("//input[@value='40083 120198']")
                shit2=driver.find_element_by_xpath("//input[@value='60279 120198']")
                shit1.click()
                shit2.click()
                driver.find_element_by_xpath("//input[@value='Register']").click()
                break
            except NoSuchElementException:
                try:
                    print('no 46 yet, trying again....')
                    switch+=1
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.back()
                    driver.find_element_by_link_text("I Agree to the Above Statement").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_name("p_term").find_element_by_xpath\
                    ("//option[@value='120198']").click()
                    driver.find_element_by_xpath("//input[@value='Submit']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//option[@value='STAT']").click()
                    driver.find_element_by_xpath("//input[@value='Course Search']").click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath("//tbody/tr[13]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()'''
        


func1()

print('Course selected')
