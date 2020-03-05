from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#login_form input[name="login-username"]')
    LOGIN_PASS = (By.CSS_SELECTOR, '#login_form input[name="login-password"]')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#register_form input[name="registration-email"]')
    REGISTER_PASS = (By.CSS_SELECTOR, '#register_form input[name="registration-password1"]')
    REGISTER_PASS_CONFIRM = (By.CSS_SELECTOR, '#register_form input[name="registration-password2"]')

