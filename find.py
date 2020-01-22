from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

course=input("Course number?")
course=course.upper()
major=course.split()[0]
index=course.split()[1]

gce=True
register=0
limit=5

if gce:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
else:
    driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")


driver.get('https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1')
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
    driver.find_element_by_link_text("Add/Drop Classes").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("I Agree to the Above Statement").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@value='Submit']").click()
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
