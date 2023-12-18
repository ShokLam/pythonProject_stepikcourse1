import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc():
    sum_number = int(a_element) + int(b_element)
    print(a_element)
    print(b_element)
    print(sum_number)
    return sum_number

try:

    link = "https://suninjuly.github.io/selects1.html"
    chrome = webdriver.Chrome()
    chrome.get(link)
    a_element = chrome.find_element(By.ID, "num1").text
    b_element = chrome.find_element(By.ID, "num2").text
    sum_number = int(a_element) + int(b_element)

    # print(str(sum_number))

    # sum_full = f"[value='{sum(a_element + b_element)}']"
    # print(sum_full)
    select = Select(chrome.find_element(By.ID, 'dropdown')) # раскрытие списка значений
    select.select_by_value(f'{sum_number}') # выбор необходимого значения
    chrome.find_element(By.CSS_SELECTOR, "body>div>form>button").click()
finally:
    time.sleep(6)
