import time
import pandas as pd
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    driver.wait = WebDriverWait(driver,5)
    return driver
# time.sleep(5)
def lookup(driver, query):
    #home Url
    driver.get("https://www.flipkart.com/")

    box = driver.wait.until(EC.presence_of_element_located(
        (By.NAME,"q")))
    button = driver.wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME,"vh79eN")))
    box.send_keys(query)
    button.click()
    Url = driver.current_url
    return Url
def down(driver,lookup):
    #target Url
    print lookup
    driver.get(lookup)
    content = driver.find_elements(By.CSS_SELECTOR,'.col-7-12')
    rating =  driver.find_elements(By.CSS_SELECTOR,'.niH0FQ')
    pri = driver.find_elements(By.CSS_SELECTOR,'._1uv9Cb')
    phone,ram,rate,price  = [],[],[],[]

    for c in content:
        phone.append(c.find_element(By.CSS_SELECTOR,"._3wU53n").text)
        ram.append(c.find_element(By.CSS_SELECTOR,".OiPjke").text)
    for c in rating:
        rate.append(c.find_element(By.CSS_SELECTOR,'.hGSR34').text.encode('utf-8'))
    for c in pri:
        price.append(c.find_element(By.CSS_SELECTOR,'._2rQ-NK').text.encode('utf-8'))
    df = pd.DataFrame({'Phone':phone})
    df['Ram'] = ram
    df["Rating"] = rate
    df['Price'] = price
    print df
    df.to_csv('out.csv')

if __name__ == "__main__":
    driver = init_driver()
    down(driver,lookup(driver,'moto'))
    time.sleep(15)
    driver.quit()
