from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from main_project.base.base_class import Base


class Login_page(Base):
    url = 'https://app.moovenow.online/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sum_money = "3333"
    a_park = "A park"
    word_assert = "Plan your trip easily"
    bar = "Bar"

    next_button = "//button[contains(@class, 'button')]"
    loc_money = "//input[@type='number']"
    moscow = "//div[contains(@class, 'tag__container')]"
    loc_tag = "//input[@placeholder='Enter tags you entered in (search...)']"
    loc_button_bar = "//div[contains(@class, 'tag__container')]"
    loc_button_amusement_park = "//div[contains(@class, 'tag__container')]"
    main_word = "//p[@class='sc-FIATH MtuWj sc-beqWaB gtzmME paragraph main__welcome-title']"

    # Getters

    def get_loc_money(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_money)))

    def get_next_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.next_button)))

    def get_moscow(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.moscow)))

    def get_loc_tag(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_tag)))

    def get_loc_button_amusement_park(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_button_amusement_park)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_sum_money(self, sum_money):
        self.get_loc_money().send_keys(sum_money)
        print("Input sum money")

    def click_moscow(self):
        self.get_moscow().click()
        print("Click Moscow")

    def input_loc_tag(self, bar):
        self.get_loc_tag().send_keys(bar)
        print("Input tag")

    def click_loc_button_amusement_park(self):
        self.get_loc_button_amusement_park().click()
        print("Click Amusement park")

    def click_next_button(self):
        self.get_next_button().click()
        print("Click next")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_sum_money(self.sum_money)
        self.click_next_button()
        self.click_moscow()
        self.click_next_button()
        self.input_loc_tag(self.bar)
        self.click_loc_button_amusement_park()
        self.click_next_button()
        self.assert_word(self.get_main_word(), self.word_assert)
