from base.custom_driver import CustomDriver
from utilities.custom_logger import CustomLogger as cl
import logging
from utilities.read_excel_data import writeExcelData

class TestStatus(CustomDriver):

    log = cl.customLog(logging.DEBUG)
    count = 2

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("Verification passed")
                else:
                    self.resultList.append("FAIL")
                    self.log.error("***VERIFICATION FAILED***")
            else:
                self.resultList.append("FAIL")
                self.log.error("***VERIFICATION FAILED***")
        except:
            self.log.error("***EXCEPTION OCCURED***")

    def mark(self,result):
        self.setResult(result)

    def mark_final(self, testcase, result, filepath):
        self.setResult(result)
        if "FAIL" in self.resultList:
            self.log.error("***"+ testcase+ "FAILED ***")
            self.screenShot()
            writeExcelData(filepath,self.count,3,"Test Failed")
            self.count+=1
            self.resultList.clear()
            assert True == False

        else:
            self.log.info(testcase + " PASSED")
            writeExcelData(filepath, self.count, 3, "Test Passed")
            self.count+=1
            self.resultList.clear()
            assert True == True



