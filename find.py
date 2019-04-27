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

driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
driver.get('https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1')
driver.implicitly_wait(7.5)

driver.find_element_by_id("netid").send_keys('jwang242')
driver.find_element_by_id("easpass").send_keys('Xawjx1996928!')
driver.find_element_by_name("BTN_LOGIN").click()
driver.implicitly_wait(10)
driver.find_element_by_id("netid").send_keys('jwang242')
driver.find_element_by_id("easpass").send_keys('Xawjx1996928!')
driver.find_element_by_name("BTN_LOGIN").click()
driver.implicitly_wait(10)

driver.find_element_by_link_text("Registration & Records").click()
driver.implicitly_wait(10)

def find():
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
    driver.find_element_by_xpath("//option[@value='"+major+"']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    i=3
    try:
        while True:
            number=driver.find_element_by_xpath("//html/body/div[3]/table[2]/tbody/tr["+str(i)+"]/td[1]").text
            if index==number:
                break
            i+=1
    except NoSuchElementException:
        print('Index does not exist')
        driver.quit()

    print(i)

find()

while True:
    course=input("Course number?")
    if course==0:
        break
    course=course.upper()
    major=course.split()[0]
    index=course.split()[1]

    driver.find_element_by_xpath("//html/body/div[1]/div[2]/span/map/p/table/tbody/tr[1]/td/table/tbody/tr/td[7]/a").click()
    find()

