#!/usr/bin/python
# -*- Coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def setter(driver, text, url='https://www.google.com/', input_class="gLFyf.gsfi"):
    driver.get(url)
    WebDriverWait(driver, timeout=30).until(
        EC.presence_of_element_located((By.CLASS_NAME, input_class))
    )
    driver.find_element_by_class_name(input_class).send_keys(text)
    driver.find_element_by_class_name(input_class).submit()

def getter(driver, tgt_tag="cite"):
    html = driver.page_source
    bf = BeautifulSoup(html, "lxml")
    WebDriverWait(driver, timeout=30).until(
        EC.presence_of_element_located((By.TAG_NAME, tgt_tag))
    )
    vals = bf.find_all(tgt_tag)
    urls = [v.get_text().split(" › ")[0] for v in vals]
    return urls

def executor(driver, text):
    setter(driver, text)
    # time.sleep(wait)
    urls = getter(driver)
    print("INFO: ", text, "のurlを%s件取得"%len(urls))
    return urls

if __name__ == "__main__":
    pass