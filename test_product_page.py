from time import sleep

import pytest
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



@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
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


link_of_guest = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.guest
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


# @pytest.mark.skip
@pytest.mark.guest
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# @pytest.mark.skip
@pytest.mark.guest
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    sleep(1)
    page.should_disappear_success_message()



# @pytest.mark.guest
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     # 1 Открываем страницу товара
#     page = ProductPage(browser, link_of_guest)
#     page.open()
#     # 2 Добавляем товар в корзину
#     page.add_to_basket()
#     # 3 Проверяем, что нет сообщения об успехе с помощью is_not_element_present
#     assert page.not_message_success_add_to_cart_present(), 'Тестовый гость видит сообщение о добавлении в корзину'
#
# @pytest.mark.guest
# def test_guest_cant_see_success_message(browser):
#     # 1 Открываем страницу товара
#     page = ProductPage(browser, link_of_guest)
#     page.open()
#     # 2 Проверяем, что нет сообщения об успехе с помощью is_not_element_present
#     assert page.not_message_success_add_to_cart_present(), 'Тестовый гость увидет сообщение о успехе'
#
# @pytest.mark.guest
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     # 1 Открываем страницу товара
#     page = ProductPage(browser, link_of_guest)
#     page.open()
#     # 2 Добавляем товар в корзину
#     page.add_to_basket()
#     sleep(5)
#     # 3 Проверяем, что нет сообщения об успехе с помощью is_disappeared
#     assert page.not_message_success_add_to_cart_disappeared(), 'тестовое сообщение НЕ исчезло после добавления товара в корзину'






























