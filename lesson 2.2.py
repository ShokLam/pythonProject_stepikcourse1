from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x_value):
    return str(math.log(abs(12 * math.sin(int(x_value)))))


try:

    link = "http://suninjuly.github.io/get_attribute.html"
    chrome = webdriver.Chrome()
    chrome.get(link)
    x_element = chrome.find_element(By.ID, "treasure")
    x_value = x_element.get_attribute("valuex")
    print(x_value)
    print(type(x_value))

    y = calc(x_value)
    y_element = chrome.find_element(By.ID, "answer")
    y_element.click()
    y_element.send_keys(f"{y}")

    chrome.find_element(By.ID, "robotCheckbox").click()
    chrome.find_element(By.ID, "robotsRule").click()
    chrome.find_element(By.XPATH, "/html/body/div/form/div/div/button").click()
finally:
    time.sleep(6)
