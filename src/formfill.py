#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from json import *
from webdriver_manager.chrome import ChromeDriverManager

#getting chromedriver from webdriverpackage-manager 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("site")

#login credentials
with open(r"login.file", 'r') as login:
    stuff = login.read().split('\n')
    EMAIL = stuff[0]
    PW = stuff[1]


def fill():
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "loginfmt")))
        emil = driver.find_element('name','loginfmt')
        emil.send_keys(EMAIL)
        btn = driver.find_element('id','idSIButton9')
        btn.click()

        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "passwd")))
        pw = driver.find_element('name', 'passwd')
        pw.send_keys(PW)
        sleep(1)

        btn2 = driver.find_element('id','idSIButton9')
        btn2.click()
        driver.back()
        
        element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-format-content"))
        )

        questions = 'sum'
        num = 1
        while questions:
            num += 1
            if num == 7:
                questions = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div/div[2]/div/div[2]')
                questions.click()
            try:
                questions = driver.find_element(By.XPATH,f'/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[{num}]/div/div[2]/div/div[1]')
                questions.click()
            except:
                questions = ''
            
        try:
            driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()
        except:
            raise Exception("Something went wrong. Ensure your password is in password.pw") 
        sleep(5)
        print("Completed successfully")
fill()

driver.quit()