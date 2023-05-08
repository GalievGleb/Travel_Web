import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.pages.finish_page import Finish_page
from main_project.pages.login_page import Login_page
from main_project.pages.main_page import Main_page


def test_choice_cart():
    driver = webdriver.Chrome()

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    f = Finish_page(driver)
    f.finish()

    time.sleep(3)
    driver.quit()
