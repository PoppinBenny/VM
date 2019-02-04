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

lab=[68966,68970,68983,68984,68991,68998,68999,69000,69007]
disc=[68948,68949,68958,68959,68961,68962,68963,68964,68977]
#lecture TR12-1

def func1():
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
    driver.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys('ylan6')
    driver.find_element_by_id("easpass").send_keys('d39-ype-Aqy')
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
    driver.find_element_by_xpath("//option[@value='PHYS']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//tbody/tr[9]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    b=False
    while True:
        print('4')
        for i in lab:
            for j in disc:
                driver.implicitly_wait(0.1)
                try:
                    str1="//input[@value='"+str(i)+" 120191']"
                    str2="//input[@value='"+str(j)+" 120191']"
                    shit1=driver.find_element_by_xpath("//input[@value='68939 120191']")
                    shit2=driver.find_element_by_xpath(str1)
                    shit3=driver.find_element_by_xpath(str2)
                    shit1.click()
                    shit2.click()
                    shit3.click()
                    driver.find_element_by_xpath("//input[@value='Register']").click()
                    b=True
                except NoSuchElementException:
                    try:
                        switch+=1
                        if switch==81:
                            switch=0
                            driver.back()
                            driver.find_element_by_xpath("//tbody/tr[9]/td/form/input[@value='View Sections']").click()
                    except NoSuchElementException:
                        time.sleep(30)
                        driver.close()
                        func1()
        if b==True:
            break


func1()

print('Course selected')
