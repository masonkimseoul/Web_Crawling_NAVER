from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip


def nid_login():
    log_in_url = "https://nid.naver.com/nidlogin.login"

    driver = webdriver.Chrome('/Users/user/Desktop/Coding/chromedriver')
    driver.get(log_in_url)
    driver.implicitly_wait(3)

    while True:
        tag_id = driver.find_element_by_name('id')
        tag_pw = driver.find_element_by_name('pw')

        tag_id.click()
        user_id = input("id=")
        pyperclip.copy(user_id)
        tag_id.send_keys(Keys.CONTROL, 'v')

        tag_pw.click()
        user_pw = input("pw=")
        pyperclip.copy(user_pw)
        tag_pw.send_keys(Keys.CONTROL, 'v')

        pyperclip.copy('')
        driver.find_element_by_id('log.login').click()

        if driver.current_url != 'https://nid.naver.com/nidlogin.login':
            break

        tag_id.clear()
        tag_pw.clear()

    driver.find_element_by_id("new.dontsave").click()

    return driver
