from PythonSelFramework.utilities.BaseClass import BaseClass
import pytest
from PythonSelFramework.pageObjects.HomePage import HomePage
from PythonSelFramework.TestData.HomePageData import HomePageData

class TestTwo(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name"+getData["name"])
        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["Password"])
        homepage.getCheckBox().click()
        # select class provide the methods to handle options in dropdown
        self.selectOptionByText(homepage.getDropDown(),"Female")
        homepage.getSubmit().click()
        message = homepage.getAlert().text
        # XPATH-//*[contains(@class,'alert-success')
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase03"))
    def getData(self,request):
        return request.param