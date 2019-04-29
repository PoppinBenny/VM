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


disc1=[65053,35926,35954,35956,35923,58757,62140,62833,62834,65051]
lecture1=[35917,35919,72271,72273]
disc2=[63737,63735,63736,63738,63739]
lecture2=[63733,64513,72275,72276]


def func1():
    driver.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys('jundong2')
    driver.find_element_by_id("easpass").send_keys('Tedjd1485466482!')
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)
    driver.find_element_by_id("netid").send_keys('jundong2')
    driver.find_element_by_id("easpass").send_keys('Tedjd1485466482!')
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
    driver.find_element_by_xpath("//option[@value='CS']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//tbody/tr[12]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    switch=0
    while True:
        if switch%20<19:
            print(17)
            for i in lecture1:
                for j in disc1:
                    driver.implicitly_wait(0.15)
                    try:
                        str1="//input[@value='"+str(i)+" 120198']"
                        str2="//input[@value='"+str(j)+" 120198']"
                        shit1=driver.find_element_by_xpath(str1)
                        shit2=driver.find_element_by_xpath(str2)
                        shit1.click()
                        shit2.click()
                        driver.find_element_by_xpath("//input[@value='Register']").click()
                        driver.implicitly_wait(10)
                        driver.back()
                        switch=3
                    except NoSuchElementException:
                        pass
            switch+=1
            if switch%20<19:
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[12]/td/form/input[@value='View Sections']").click()
            elif switch%20==19:
                driver.back()
                driver.find_element_by_xpath("//tbody/tr[13]/td/form/input[@value='View Sections']").click()
        elif switch%20==19:
            shit1=driver.find_element_by_xpath("//input[@value='63733 120198']")
            shit2=driver.find_element_by_xpath("//input[@value='63737 120198']")
            shit1.click()
            shit2.click()
            driver.find_element_by_xpath("//input[@value='Register']").click()
            driver.implicitly_wait(10)
            driver.back()
            driver.back()
            driver.find_element_by_xpath("//tbody/tr[12]/td/form/input[@value='View Sections']").click()
            switch+=1



func1()

print('Course selected')
