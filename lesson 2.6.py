import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)

driver.find_element(By.XPATH, "/html/body/form/div/div/button").click()

alert = driver.switch_to.alert
alert.accept()

x_val = driver.find_element(By.ID,"input_value")
result_x = x_val.text
y = calc(result_x)
answer = driver.find_element(By.ID, "answer")
answer.send_keys(y)
driver.find_element(By.XPATH, "/html/body/form/div/div/button").click()
time.sleep(5)
# alert = driver.switch_to.alert # переключение на диалоговое окно
# alert_text = alert.text  #
#
#
# confirm = driver.switch_to.alert
# confirm.accept()  # согласиться с условиями диалогового окна
# confirm.dismiss() # отказаться от условий в диалоговом окне
#
# prompt = driver.switch_to.alert
# prompt.send_keys("My answer") # вставить в диалоговое окно текст
# prompt.accept()