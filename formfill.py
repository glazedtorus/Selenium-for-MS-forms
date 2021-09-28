import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'o=your path here')
driver.get("your form here")

def fill():
    for i in  range(1,6):
        radiobuttons = driver.find_elements_by_css_selector("input[type='radio'][value='No']")
        radiobuttons[i].click()

    button6 = driver.find_element_by_css_selector("input[type='radio'][aria-checked='false'][value='Yes']")
    button6.click()

    for x in range(1,4):
        lastbuttons = driver.find_elements_by_css_selector("input[type='radio'][value='No']")
        lastbuttons[x].click()

    button10 = driver.find_element_by_css_selector("input[type='radio'][aria-checked='false'][value=' ']")
    button10.click()

    submit = driver.find_elements_by_css_selector('.button-content')
    submit[1].click()

def rightSite():
    if "2021" in driver.title:
        return True
        fill()
    else:
        return False
rightSite()

driver.quit()