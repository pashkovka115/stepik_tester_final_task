import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, BasketPageLocators



class BasePage:
    browser: webdriver.Chrome


    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.maximize_window()
        self.browser.implicitly_wait(timeout)
        self.url = url


    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        """ Элемент появится в течении времени не явного ожидания """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def is_not_element_present(self, how, what, timeout=4):
        """ Элемент не появляется в течении timeout секунд """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False


    def is_disappeared(self, how, what, timeout=4):
        """ Элемент исчезает в течении timeout секунд """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.LINK_BASKET)
        link.click()


    def empty_basket(self):
        text_basket = self.browser.find_element(*BasketPageLocators.BASKET).text
        assert 'basket is empty' in text_basket, f'Корзина НЕ пуста. Ожидается "basket is empty". Факт: {text_basket}'



    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def current_language(self):
        """ Язык в настройках браузера (не сайта) """
        return self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
