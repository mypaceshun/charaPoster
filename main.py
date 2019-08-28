#!/usr/bin/env python
import os
import time
import chromedriver_binary  # noqa :F401
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from charaPoster.poster import Poster

USERNAME = os.environ.get("CHARAPOSTER_USERNAME", "username")
PASSWORD = os.environ.get("CHARAPOSTER_PASSWORD", "password")


def main():
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    p = Poster(driver)
    post_list = [1,2,3]
    p.post(post_list)
    time.sleep(10)

if __name__ == '__main__':
    main()
