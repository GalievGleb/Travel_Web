from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from main_project.base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = "//div[@class='sc-cbelXg pIDKX activity-card__square-button']"
    basket = "//img[@class='selected-activity__photo']"

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_basket(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.basket)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product 1")

    def click_basket(self):
        self.get_basket().click()
        print("Click basket")

    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        time.sleep(3)
        self.click_basket()
        time.sleep(3)
