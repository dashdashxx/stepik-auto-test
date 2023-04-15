from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, 'num1')
    num1 = num1.text
    num2 = browser.find_element(By.ID, 'num2')
    num2 = num2.text
    sum = int(num1) + int(num2)
    sum = str(sum)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(sum)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()