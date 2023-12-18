import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

driver.find_element(By.XPATH, "/html/body/form/div/div/button").click()
first_window = driver.window_handles[0]
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x_val = driver.find_element(By.ID,"input_value")
result_x = x_val.text
y = calc(result_x)
answer = driver.find_element(By.ID, "answer")
answer.send_keys(y)
driver.find_element(By.XPATH, "/html/body/form/div/div/button").click()
time.sleep(3)




