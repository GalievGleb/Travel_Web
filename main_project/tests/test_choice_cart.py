import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.pages.login_page import Login_page


def test_choice_cart():
    driver = webdriver.Chrome()

    print("Start Test")

    login = Login_page(driver)
    login.authorization()
    #
    # button_login = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tag__container')]")))
    # button_login.click()
    #
    # print("Click Moscow")
