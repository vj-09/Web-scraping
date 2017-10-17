import time
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
    driver.get("https://www.flickr.com/")

    box = driver.wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME,"autosuggest-selectable-item")))
    button = driver.wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME,"search-icon-button")))
    box.send_keys(query)
    button.click()
    Url = driver.current_url
    return Url
def down(driver,lookup):
    #target Url
    print lookup
    driver.get(lookup)
    content = driver.find_elements_by_css_selector('div.photo-list-photo-view ')
    for c in content:
        img_url = c.value_of_css_property("background-image")
        img_url = img_url[5:-1]
        urllib.urlretrieve(img_url, img_url.split("/")[-1])
if __name__ == "__main__":
    driver = init_driver()
    data = raw_input('Enter the term to be scraped')
    down(driver,lookup(driver,data))
    time.sleep(15)
    driver.quit()
