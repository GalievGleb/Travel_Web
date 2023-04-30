from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.base.base_class import Base


class Login_page(Base):
    url = 'https://app.moovenow.online/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sum_money = "3333"
    a_park = "A park"
    button = "//button[contains(@class, 'button')]"
    loc_money = "//input[@type='number']"
    moscow = "//div[contains(@class, 'tag__container')]"
    input_a_park = "//input[@placeholder='Enter tags you entered in (search...)']"
    click_button_amusement_park = "//div[contains(@class, 'tag__container')]"

    # Getters

    def get_loc_money(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_money)))

    def get_next_button_money(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button)))

    def get_moscow(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.moscow)))

    def get_next_button_city(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button)))

    def get_input_a_park(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.input_a_park)))

    def get_click_button_amusement_park(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_button_amusement_park)))

    def get_next_button_tags(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button)))

    # Actions

    def input_sum_money(self, sum_money):
        self.get_loc_money().send_keys(sum_money)
        print("Input sum money")

    def click_next_button_money(self):
        self.get_next_button_money().click()
        print("Click next")

    def authorization(self):
        user_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='number']")))  # обращение к элемену через id
        user_name.send_keys(sum_money)
        print("Input sum money")

        button_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-fbJfA eWVBmF button']")))
        button_login.click()
        print("Click Next Button")

        button_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-ktEKTO gaaqEw tag__container']")))
        button_login.click()
        print("Click Moscow")

        button_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-fbJfA eWVBmF button']")))
        button_login.click()
        print("Click Next Button")

        user_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter tags you entered in (search...)']")))
        user_name.send_keys(a_park)
        print("Input a park")

        time.sleep(2)

        button_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='sc-ktEKTO gaaqEw tag__container' and contains(text(), 'Amusement park')]")))
        button_login.click()
        print("Click Amusement park")

        time.sleep(2)

        button_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-fbJfA eWVBmF button']")))
        button_login.click()
        print("Click Next Button")

        time.sleep(10)


test = Login_page(Base)
test.authorization()
