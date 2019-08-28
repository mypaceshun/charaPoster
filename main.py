#!/usr/bin/env python
import os
import time
import chromedriver_binary  # noqa :F401
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from charaPoster.poster import Poster

USERNAME = os.environ.get("CHARAPOSTER_USERNAME", "username")
PASSWORD = os.environ.get("CHARAPOSTER_PASSWORD", "password")


def main():
    # options = ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    options = FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_options=options,
              executable_path='./bin/geckodriver')
    p = Poster(driver)
    post_list = [
            {'event_value': 9,
            'member': '中井りか',
            'bu': 5,
            'num': 3},
            {'event_value': 19,
            'member': '中井りか',
            'bu': 3,
            'num': 2},
            ]
    p.post(USERNAME, PASSWORD, post_list)
    time.sleep(10)

if __name__ == '__main__':
    main()
