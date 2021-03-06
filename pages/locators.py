from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#login_form input[name="login-username"]')
    LOGIN_PASS = (By.CSS_SELECTOR, '#login_form input[name="login-password"]')

    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_link')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'form#register_form #id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, 'form#register_form #id_registration-password1')
    REGISTER_PASS_CONFIRM = (By.CSS_SELECTOR, 'form#register_form #id_registration-password2')
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, 'form#register_form button')



class ProductPageLocators:
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, '#add_to_basket_form')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')

    MESSAGES_INFO = (By.CSS_SELECTOR, '#messages > div')
    MESSAGES_PRODUCT_TITLE = (By.CSS_SELECTOR, '#messages > div:first-child div.alertinner strong')
    MESSAGES_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages > div:last-child div.alertinner strong')

    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'h1 + p')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")



class BasketPageLocators:
    LINK_BASKET = (By.XPATH, '//div[contains(@class, "basket-mini")]//a')
    BASKET = (By.XPATH, '//div[@id="content_inner"]')
