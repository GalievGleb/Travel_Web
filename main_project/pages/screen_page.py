from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from main_project.base.base_class import Base
from main_project.utilities.logger import Logger


class Screen_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = "//div[@title='Urban Kitchen Кафе / Гастропаб / Кулинарная студия']//div[@class='sc-cbelXg " \
                       "pIDKX activity-card__square-button']"

    basket = "//img[@class='selected-activity__photo']"

    # Methods

    def screen(self):

        Logger.add_start_step(method="screen")
        self.get_current_url()
        self.assert_url('https://app.moovenow.online/')
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="screen")
