import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer").send_keys(y)
    time.sleep(2)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    time.sleep(2)
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    robot_radiobutton.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()