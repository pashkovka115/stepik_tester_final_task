from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()


    def should_be_message_add_to_basket(self):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES_INFO)
        assert messages, f'Сообщений о добавлении в корзину нет {self.browser.current_url}'


    def get_messages_from_basket(self):
        return self.browser.find_elements(*ProductPageLocators.MESSAGES_INFO)


    def get_product_title_of_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text.strip()


    def get_product_title_from_message_basket(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGES_PRODUCT_TITLE).text.strip()


    def get_product_price_of_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()


    def get_product_price_from_message_basket(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGES_PRODUCT_PRICE).text.strip()


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should not disappear"


    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappear"


    def title_page_mutch_title_basket(self):
        title_page = self.get_product_title_of_page()
        title_basket = self.get_product_title_from_message_basket()

        assert title_page == title_basket, f'Название товара не соответствует названию в корзине {self.browser.current_url}. Ожидается: "{title_page}". Фактически: "{title_basket}"'


    def price_page_mutch_price_basket(self):
        price_page = self.get_product_price_of_page()
        price_basket = self.get_product_price_from_message_basket()

        assert price_page == price_basket, f'Цена на странице не соответствует цене в корзине {self.browser.current_url}. Ожидается: {price_page}. Фактически: {price_basket}"'
