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



class ProductPageLocators:
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, '#add_to_basket_form')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')

    MESSAGES_INFO = (By.CSS_SELECTOR, '#messages > div')
    MESSAGES_PRODUCT_TITLE = (By.CSS_SELECTOR, '#messages > div:first-child div.alertinner strong')
    MESSAGES_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages > div:last-child div.alertinner strong')

    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'h1 + p')
