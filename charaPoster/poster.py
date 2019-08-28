from selenium.webdriver.common.by import By

BASE_URL = "https://akb48.chara-ani.com/"

class Poster:
    def __init__(self, driver):
        self.driver = driver

    def post(self, post_list):
        d = self.driver
        d.get(BASE_URL)
