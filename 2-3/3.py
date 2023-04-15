from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    window = browser.window_handles[1]
    browser.switch_to.window(window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    ele = browser.find_element(By.ID, 'answer')
    ele.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()