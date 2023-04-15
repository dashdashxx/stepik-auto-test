from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    fn = browser.find_element(By.NAME, 'firstname')
    fn.send_keys('Jerma')
    ln = browser.find_element(By.NAME, 'lastname')
    ln.send_keys('985')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('jerma985@mail.com') 
    file_path = os.path.join(current_dir, 'file.txt') 
    element = browser.find_element(By.NAME, 'file')  
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()