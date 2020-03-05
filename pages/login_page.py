from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'URL не соответствует странице входа'


    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM)


    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
