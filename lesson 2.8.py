from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(driver, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = WebDriverWait(driver, 13).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
button.click()

x_val = driver.find_element(By.ID,"input_value")
result_x = x_val.text
y = calc(result_x)
answer = driver.find_element(By.ID, "answer")
answer.send_keys(y)
solve = driver.find_element(By.XPATH, '//*[@id="solve"]')
solve.click()


time.sleep(4)