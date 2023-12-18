from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work');") # изменяем заголовок страницы и посылаем предупреждение о том что работает робот

link = "http://suninjuly.github.io/execute_script.html"
driver.get(link)
x = driver.find_element(By.ID, value="input_value")
x_value = x.text
y = calc(x_value)
button_answer = driver.find_element(By.ID, "answer")
button_answer.send_keys(y)
button_check_robot = driver.find_element(By.ID, "robotCheckbox").click()

button_rule_robot = driver.find_element(By.ID, "robotsRule")
driver.execute_script("return arguments[0].scrollIntoView(true);", button_rule_robot)
button_rule_robot.click()

button_submit = driver.find_element(By.XPATH, "/html/body/div/form/button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
button_submit.click()

# time.sleep(5)
