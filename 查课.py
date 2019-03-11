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



course=input("Course number?")
course=course.upper()
major=course.split()[0]
index=course.split()[1]

driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
driver.get('https://courses.illinois.edu/schedule/DEFAULT/DEFAULT')
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/a").click()


i=1
try:
    while True:
        m=driver.find_element_by_xpath("//*[@id='term-dt']/tbody/tr["+str(i)+"]/td[1]").text
        if m==major:
            break
        i+=1
except NoSuchElementException:
    print('Major does not exist')
    driver.quit()

driver.find_element_by_xpath("//*[@id='term-dt']/tbody/tr["+str(i)+"]/td[2]/a").click()

driver.implicitly_wait(7)
i=1
try:
    while True:
        t=driver.find_element_by_xpath("//*[@id='default-dt']/tbody/tr["+str(i)+"]/td[1]").text
        if course==t:
            break
        i+=1
except NoSuchElementException:
    print('Index does not exist')
    driver.quit()

print(i+2)
