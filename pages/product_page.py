from time import sleep

from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    # TODO Дописать методы-проверки.

    # Сообщение о том, что товар добавлен в корзину
    # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
    # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

        # sleep(120)


    def should_be_message_add_to_basket(self):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES_INFO)
        assert len(messages) == 3, f'Количество сообщений о добавлении в корзину не совпадает {self.browser.current_url}'


    def right_product_added(self):
        """артикул в корзине не выводится для сверки"""
        assert False


    def cost_basket_same_message(self):
        """Осуществить тест после изменений"""
        assert False



























