from base.custom_driver import CustomDriver
from utilities.custom_logger import CustomLogger as cl
import logging

class LoginPage(CustomDriver):

    log = cl.customLog(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def clickLogin(self):
        self.clickElement("//a[contains(text(),'Login')]", "xpath")

    def enterEmail(self , username):
        email_field = self.waitForElement("user_email")
        self.sendKeys(username, "user_email")

    def enterPassword(self, password):
        self.sendKeys(password, "user_password")

    def clickLoginButton(self):
        self.clickElement("//input[@value = 'Log In']", "xpath")

    def verifyLoginSuccesful(self):
        result = self.isElementPresent("gravatar", "class_name")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password.')]","xpath")
        return result

    def verifyTitle(self):
        title = self.getTitle()
        if 'Google' in title:
            return True
        else:
            return False

    def login(self, username, password):
        self.clickLogin()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()













