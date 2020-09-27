from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
from utilities.read_excel_data import readExcelData
from ddt import ddt,data,unpack

@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class TestLogin(unittest.TestCase):

    filepath = "E:\\Workspace_python\\AutoFramework\\excel_data.xlsx"

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get('https://learn.letskodeit.com/p/practice')
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1)
        self.lp.login("test@email.com" , "abcabc")
        result2 = self.lp.verifyLoginSuccesful()
        self.ts.mark_final("test_validLogin",result2,self.filepath)
        time.sleep(10)

    @data(*readExcelData("E:\\Workspace_python\\AutoFramework\\excel_data.xlsx"))
    @unpack
    @pytest.mark.run(order=1)
    def test_invalidLogin(self, username, password):

        self.driver.get('https://learn.letskodeit.com/p/practice')
        self.lp.login(username, password)
        result = self.lp.verifyLoginFailed()
        self.ts.mark_final("test_invalidLogin", result, self.filepath)











