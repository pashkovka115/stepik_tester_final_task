import time
from random import randint

import pytest

from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

links = [
    'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',

    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

link_of_guest = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'



@pytest.mark.guest
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()



@pytest.mark.guest
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1)
    page.should_disappear_success_message()



@pytest.mark.login_link
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()



@pytest.mark.login_link
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()



def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # 1 Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # 2 Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    # 3 Ожидаем, что в корзине нет товаров
    # 4 Ожидаем, что есть текст о том что корзина пуста
    page.empty_basket()


@pytest.mark.register_and_by
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = 'uyf' + str(time.time()) + "@fakemail.org"
        passwd = 'adsv' + str(randint(111111111, 9999999999)) + 'fr'
        # 1 открыть страницу регистрации
        page = LoginPage(browser, link)
        page.open()
        # 2 зарегистрировать нового пользователя
        page.register_new_user(email=email, password=passwd)
        # 3 проверить, что пользователь залогинен
        page.is_element_present(*LoginPageLocators.LOGOUT_LINK)



    @pytest.mark.guest
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


    # @pytest.mark.parametrize('link', links)
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_message_add_to_basket()

        title_page = page.get_product_title_of_page()
        title_basket = page.get_product_title_from_message_basket()

        price_page = page.get_product_price_of_page()
        price_basket = page.get_product_price_from_message_basket()

        assert title_page == title_basket, f'Название товара не соответствует названию в корзине {link}. Ожидается: "{title_page}". Фактически: "{title_basket}"'
        assert price_page == price_basket, f'Цена на странице не соответствует цене в корзине {link}. Ожидается: {price_page}. Фактически: {price_basket}"'



# #######################################################################################
# На это не смотри, это для будущих побед
# @pytest.mark.login
# @pytest.mark.skip
# class TestLoginFromProductPage():
#     """ Это только пример """
#
#
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         # self.product = ProductFactory(title="Best book created by robot")
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#
#
#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
