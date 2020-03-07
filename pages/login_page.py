from time import sleep

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


    def register_new_user(self, email, password):

        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        password_input.clear()
        password_input.send_keys(password)

        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONFIRM)
        confirm_password.clear()
        confirm_password.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        button.click()




