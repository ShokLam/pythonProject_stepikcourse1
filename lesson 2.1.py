from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:

    link = "https://suninjuly.github.io/math.html"
    chrome = webdriver.Chrome()
    chrome.get(link)
    x_element = chrome.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    y = calc(x)
    y_element = chrome.find_element(By.ID, "answer")
    y_element.click()
    y_element.send_keys(f"{y}")

    chrome.find_element(By.ID, "robotCheckbox").click()
    chrome.find_element(By.ID, "robotsRule").click()
    chrome.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
finally:
    time.sleep(9)

