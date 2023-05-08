import pytest


# @pytest.fixture()
# def set_up():
#     print("Star test")
#     driver = webdriver.Chrome()
#     url = 'https://www.saucedemo.com/'
#     self.driver.get(self.url)
#     self.driver.maximize_window()
#     yield
#     print("Finish test")
#   Причины по которым мы не создаем данный файл для экнономии места потому что: 1. Нельзя перед выполнением теста в данном случае
#   отправить HTTP запрос-проверить запрос-поработать с ним. 2. Не можем запускать сразу несколько тестов.

@pytest.fixture(scope="module")
def set_grope():
    print("Enter system")
    yield
    print("Exit system")
# Отрабатывается всего раз, перед запуском всех методов всех тестов "Enter system" будет у первого теста, "Exit system" у 3