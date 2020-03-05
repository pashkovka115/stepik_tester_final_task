from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    browser: webdriver.Chrome

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True