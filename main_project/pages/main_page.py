from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from main_project.base.base_class import Base
from main_project.utilities.logger import Logger


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = "//div[@title='Urban Kitchen Кафе / Гастропаб / Кулинарная студия']//div[@class='sc-cbelXg pIDKX activity-card__square-button']"
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

        Logger.add_start_step(method="select_product")
        self.get_current_url()
        self.click_select_product_1()
        time.sleep(3)
        self.click_basket()
        time.sleep(3)
        Logger.add_end_step(url=self.driver.current_url, method="select_product")

