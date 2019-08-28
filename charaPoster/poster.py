import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://akb48.chara-ani.com/"


class Poster:
    def __init__(self, driver):
        self.driver = driver

    def post(self, username, password, post_list):
        self._move_post_page()
        for item in post_list:
            self._add_item(item)
        self._post_items(username, password)

    def _move_post_page(self):
        d = self.driver
        d.get(BASE_URL)
        main_btn_el = d.find_element(By.CLASS_NAME, 'main_btn01')
        main_btn_el.click()
        check_box_el = d.find_element(By.NAME, 'q')
        check_box_el.click()
        submit_button_el = d.find_element(By.ID, 'ibtSubmit')
        submit_button_el.click()

    def _add_item(self, item):
        d = self.driver
        value = str(item['event_value'])
        member = item['member']
        bu = '第{}部'.format(item['bu'])
        num = str(item['num'])

        events_el = d.find_element(By.ID, 'ddlEvents')
        select_event_el = Select(events_el)
        select_event_el.select_by_value(value)
        disp_el = d.find_element(By.ID, 'btnDisp')
        self._click_image_button(disp_el)

        table_el = d.find_element(By.ID, 'dlstItem')
        td_els = table_el.find_elements(By.TAG_NAME, 'td')
        for td_el in td_els:
            if member in td_el.text and bu in td_el.text:
                select_el = td_el.find_element(By.TAG_NAME, 'select')
                td_select_el = Select(select_el)
                td_select_el.select_by_value(num)

    def _post_items(self, username, password):
        d = self.driver
        submit_btn_el = d.find_element(By.ID, 'ibtnConfirm')
        self._click_image_button(submit_btn_el)

        # login
        username_el = d.find_element(By.ID, 'txID')
        if username_el is not None:
            username_el.send_keys(username)
            password_el = d.find_element(By.ID, 'txPASSWORD')
            password_el.send_keys(password)
            login_el = d.find_element(By.ID, 'btnLogin')
            self._click_image_button(login_el)

        # apply
        apply_btn_el = d.find_element(By.ID, 'btnApply')
        self._click_image_button(apply_btn_el)


    def _click_image_button(self, btn_el):
        d = self.driver
        action = ActionChains(d).move_to_element(btn_el).click(btn_el)
        action.perform()
        time.sleep(1)
