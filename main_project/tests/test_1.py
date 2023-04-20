import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_1():  # создаем класс Test_1
    def test_select_product(self):  # создаем метод
        driver = webdriver.Chrome()  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
        base_url = 'https://app.moovenow.online/'  # совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
        driver.get(base_url)  # указываем url на который мы хотим заходить
        driver.maximize_window()  # открывается браузер на максимальный экран
        time.sleep(1)

        print("Start Test")

        sum_money = "3333"
        a_park = "A park"

        user_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='number']")))  # обращение к элемену через id
        user_name.send_keys(sum_money)
        print("Input sum money")

        button_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-fbJfA eWVBmF button']")))
        button_login.click()
        print("Click Next Button Money")

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

        # succes_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        # value_succes_test = succes_test.text
        # assert value_succes_test == "YOUR CART"
        # print("Test Succes!!!!")
        #
        # time.sleep(5)


test = Test_1()  # объявляем экземпляр класса Test_1
test.test_select_product()
