from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
link =  "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
button = browser.find_element(By.ID, 'book')
button.click()

browser.find_element_by_tag_name('body').send_keys(Keys.END)
    
import math
def calc(x):
    return (math.log(abs(12*math.sin(x))))
        
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
ele = browser.find_element(By.ID, 'answer')
ele.send_keys(y)
button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
button2.click()
browser.quit()