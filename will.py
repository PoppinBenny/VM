from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os,time
from selenium.common.exceptions import TimeoutException

gce=True

major=['CS']
xuhao=['225']
crn=['35947','62139'] 

drops=[] #要加引号

account='weiyang7'
password='Wangwill0329!!!!'
n='w'
register=0
limit=5

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
                driver.find_element_by_xpath("//*[@id='action_id"+str(i-1)+"']/option[2]").click()
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

def print_error():
    status=driver.find_element_by_xpath("/html/body/div[3]/form/table[4]/tbody/tr[2]/td[1]").text
    crn=driver.find_element_by_xpath("/html/body/div[3]/form/table[4]/tbody/tr[2]/td[2]").text
    print(crn,status)

def normal(crn):
    global register
    shit1=driver.find_element_by_xpath("//input[@value='"+crn+" 120208']")
    shit1.click()
    shit2=driver.find_element_by_xpath("//input[@value='35917 120208']")
    shit2.click()
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)
    i=2
    try:
        while True:
            number=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[3]").text
            c=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[4]").text
            nu=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[5]").text
            print(c,nu,number)
            if crn==number:
                print('Course selected')
                driver.quit()
            i+=1
    except NoSuchElementException:
        print('Failed to add '+crn+' '+n)
        print_error()
        register+=1
        if register>=limit:
            print('Too many requests for '+n)
            driver.quit()
        driver.back()
    raise NoSuchElementException

def drop_mode(crn,drop):
    global register
    shit1=driver.find_element_by_xpath("//input[@value='"+crn+" 120208']")
    driver.find_element_by_xpath("//input[@value='Register']").click()
    driver.implicitly_wait(7.5)
    find_drop(drop)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_id("crn_id1").send_keys(crn)
    driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
    driver.implicitly_wait(10)
    i=2
    try:
        while True:
            number=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[3]").text
            c=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[4]").text
            nu=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[5]").text
            print(c,nu,number)
            if crn==number:
                print('Course selected')
                driver.quit()
            i+=1
    except NoSuchElementException:
        print('Failed to add '+crn+' '+n)
        print_error()
        driver.find_element_by_id("crn_id1").send_keys(drop)
        driver.find_element_by_xpath("//input[@value='Submit Changes']").click()
        driver.implicitly_wait(10)
        register+=1
        if register>=limit:
            print('Too many requests for '+n)
            driver.quit()
        driver.back()
        driver.back()
        driver.back()
        driver.back()
    raise NoSuchElementException


def func1():
    driver.get('https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1')
    driver.implicitly_wait(7.5)

    driver.find_element_by_id("netid").send_keys(account)
    driver.find_element_by_id("easpass").send_keys(password)
    driver.find_element_by_name("BTN_LOGIN").click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("Registration & Records").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Classic Registration").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Add/Drop Classes").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("I Agree to the Above Statement").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[@id='term_id']/option[1]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)

    current=int(float(driver.find_element_by_xpath("/html/body/div[3]/form/\
            table[2]/tbody/tr[1]/td[2]").text))
    maximum=int(float(driver.find_element_by_xpath("/html/body/div[3]/form/table\
            [2]/tbody/tr[4]/td[2]").text))
    if maximum-current<3 and len(drops)==0:
        print(n,"has insufficient credits. Current:",current,"Maximum:",maximum)
        driver.quit()

    if len(drops)==0:
        try:
            i=2
            repeat=False
            while True:
                c=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[4]").text
                nu=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[5]").text
                for m in major:
                    if repeat==True:
                        break
                    for x in xuhao:
                        if m==c and x==nu:
                            repeat=True
                            break
                if repeat==True:
                    print(c+nu+' already existed '+n)
                    driver.quit()
                    break
                i+=1
        except NoSuchElementException:
            driver.back()
            driver.back()
            driver.back()


    if len(drops)!=0:
        for drop in drops:
            i=2
            try:
                while True:
                    temp=driver.find_element_by_xpath("//html/body/div[3]/form/table[1]/tbody/tr["+str(i)+"]/td[3]").text
                    if drop==temp:
                        break
                    i+=1
            except NoSuchElementException:
                print('Drop index does not exist')
                driver.quit()
        driver.back()
        driver.back()
        driver.back()

    driver.find_element_by_link_text("Look-up or Select Classes").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("I Agree to the Above Statement").click()
    driver.implicitly_wait(10)
    driver.find_element_by_name("p_term").find_element_by_xpath\
    ("//option[@value='120208']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//option[@value='"+major[0]+"']").click()
    driver.find_element_by_xpath("//input[@value='Course Search']").click()
    driver.implicitly_wait(10)

    i1=find(xuhao[0])
    driver.find_element_by_xpath("//tbody/tr["+str(i1)+"]/td/form/input[@value='View Sections']").click()
    driver.implicitly_wait(10) #440 = 36, 412 = 24

    while True:
            try:
                driver.implicitly_wait(0.2)
                if len(drops)==0:
                    normal(crn[0])
                else:
                    drop_mode(crn[0],drops[0])
                break
            except NoSuchElementException:
                try:
                    print('no '+n)
                    time.sleep(6)
                    driver.back()
                    driver.find_element_by_xpath("//tbody/tr["+str(i1)+"]/td/form/input[@value='View Sections']").click()
                except NoSuchElementException:
                    time.sleep(30)
                    driver.close()
                    func1()


func1()

print('Course selected')
