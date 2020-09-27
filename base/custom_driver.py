from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.custom_logger import CustomLogger as cl
import logging
import time
import os

class CustomDriver():

    log = cl.customLog(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self):
        filename = str(time.time()*1000) + ".png"
        screenshotdir = "E:\\Workspace_python\\AutoFramework\\base\\screenshots"
        relativefilename = screenshotdir + filename
        print(relativefilename)
        try:
            self.driver.save_screenshot(relativefilename)
            self.log.info("Screen shot taken")
        except:
            self.log.error("***Exception occured screen shot not taken***")


    def getByType(self, locatorType = "id"):
        self.locatorType = locatorType.lower()
        if self.locatorType == "id":
            return By.ID
        elif self.locatorType == "name":
            return By.NAME
        elif self.locatorType == "css":
            return By.CSS_SELECTOR
        elif self.locatorType == "xpath":
            return By.XPATH
        elif self.locatorType == "tagname":
            return By.TAG_NAME
        elif self.locatorType == "link":
            return By.LINK_TEXT
        elif self.locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        elif self.locatorType == "class_name":
            return By.CLASS_NAME
        else:
            self.log.info("Locator type: "+ self.locatorType +" is NOT supported")
            return False

    def getElement(self, locator, locatorType = "id"):
        element = None
        byType = self.getByType(locatorType)
        try:
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with Locator: "+locator+" with locator type: "+locatorType)
        except:
            self.log.error("Element NOT found with Locator: "+locator+" with locator type: "+locatorType)
        return element

    def clickElement(self, locator, locatorType ="id"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element clicked with Locator: "+locator+" with locator type: "+locatorType)
        except:
            self.log.error("Element NOT clicked with Locator: " + locator + " with locator type: " + locatorType)

    def isElementPresent(self, locator, locatorType ="id"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            #element.click()
            self.log.info("Element found with Locator: "+locator+" with locator type: "+locatorType)
            return True
        except:
            self.log.error("Element NOT found with Locator: " + locator + " with locator type: " + locatorType)
            return False


    def sendKeys(self, fieldValue, locator, locatorType="id"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(fieldValue)
            self.log.info("Sent keys with Locator: " + locator + " with locator type: " + locatorType)
        except:
            self.log.error("Keys NOT sent with Locator: " + locator + " with locator type: " + locatorType)

    def getTitle(self):
        return self.driver.title

    def waitForElement(self, locator, locatorType = "id"):
        element = None
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,
                                                                                  ElementNotVisibleException,
                                                                                  ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((byType,locator)))
        return element






