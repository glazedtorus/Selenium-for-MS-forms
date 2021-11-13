from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from json import *

driver = webdriver.Chrome(executable_path=r'path')
driver.get("form")

with open('password.pw', 'r') as f:
    stuff = f.read().split('\n')
    EMAIL = stuff[0]
    PW = stuff[1]

def fill():
    try:
        elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
        )
    finally:
        emil = driver.find_element('name','loginfmt')
        emil.send_keys(EMAIL)
        btn = driver.find_element('id','idSIButton9')
        btn.click()
    try:
        elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "passwd"))
        )
    finally:
        pw = driver.find_element('name', 'passwd')
        pw.send_keys(PW)
        sleep(1)
        btn2 = driver.find_element('id','idSIButton9')
        btn2.click()
    driver.back()
fill()

def rightSite():
    try:
        if "2021" in driver.title:
            fill()
            return True
        else:
            return False
    except:
        raise Exception("Did not reach site. Try again.")
rightSite()


driver.quit()