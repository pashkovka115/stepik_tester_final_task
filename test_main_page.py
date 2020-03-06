from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # 1 Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # 2 Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # 3 Ожидаем, что в корзине нет товаров
    # 4 Ожидаем, что есть текст о том что корзина пуста
    page.empty_basket()
