import pytest

from .pages.product_page import ProductPage


# @pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # TODO пофиксить
    # https://stepik.org/lesson/201964/step/3?unit=176022
    link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_add_to_basket()
    page.right_product_added()
    page.cost_basket_same_message()

