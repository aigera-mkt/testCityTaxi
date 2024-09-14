import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Проверка наличия элемента с именем пользователя
class FindByXPath(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_find_element(self):
        confirmation_of_location = (By.XPATH, "//*[@id='__next']/header/div[1]/div/div[3]/div[1]/div[2]/div[2]/button[1]")
        driver = self.driver
        self.driver.get('https://city-mobil.ru')

        #Находим элемент Да, верно по Xpath
        element_by_xpath = WebDriverWait(driver, 10).until(EC.presence_of_element_located(confirmation_of_location))

        #Проверка, что элемент отображается на странице
        self.assertTrue(element_by_xpath.is_displayed(), "Элемент не отображается")
        print('Текст кнопки: ' + element_by_xpath.text)

        element_by_xpath.click()

    #Тест, проверяющий отображение всплывающего списка после ховера
    def test_element_interaction(self):
        banner_2 = (By.XPATH, "//*[@id='__next']/main/div/div/div[2]/div/div/div/div/a[6]/div")
        driver = self.driver
        self.driver.get('https://city-mobil.ru')
        element_interaction = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(banner_2))

         #Выполнение действия hover
        action = ActionChains(self.driver)
        action.move_to_element(element_interaction).perform()

        element_interaction.click()

    def test_after_hover(self):
        menu_item_1 = (By.XPATH, "//*[@id='__next']/header/div[2]/div/div/div/ul/li[1]/div/a/p")
        driver = self.driver
        self.driver.get('https://city-mobil.ru')

        #Ожидание элемента после ховера
        element_after_hover = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(menu_item_1))

        # Выполнение действия hover
        action = ActionChains(driver)
        action.move_to_element(element_after_hover).perform()

        element_after_hover.click()

        #Проверка отображения элемента после ховера
        self.assertTrue(element_after_hover.is_displayed(), "Элемент не отображается")

    def test_text_is_displayed(self):
        futer_element = (By.XPATH, "//*[@id='__next']/footer/div[5]/div/div/div[1]/p")
        driver = self.driver
        self.driver.get('https://city-mobil.ru')

         # Прокрутка страницы до самого низа с помощью JavaScript
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

         # Подождите немного, чтобы страница могла обновиться
        WebDriverWait(driver, 7).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
        element_in_end = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located(futer_element))

        self.assertTrue(element_in_end.is_displayed(), "Элемент не отображается")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
