from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        if self.browser == "Ie":
            return webdriver.Ie()
        elif self.browser == "chrome":
            return webdriver.Chrome()
        elif self.browser == "firefox":
            return webdriver.Firefox()
        else:
            print("Not supported browser")





