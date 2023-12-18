import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
firstname_val = "ruc"
lastname_val = "riclam"
email_val = "1@test.ru"


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)

firstname_1 = driver.find_element(By.NAME, "firstname")
firstname_1.send_keys(firstname_val)
lastname_1 = driver.find_element(By.NAME, "lastname")
lastname_1.send_keys(lastname_val)
email_1 = driver.find_element(By.NAME, "email")
email_1.send_keys(email_val)



current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file1.txt')  # добавляем к этому пути имя файла
print(file_path)
input_file = driver.find_element(By.ID, "file")
input_file.send_keys(file_path)
# time.sleep(5)
button_submit = driver.find_element(By.XPATH, "/html/body/div/form/button")
button_submit.click()
time.sleep(5)