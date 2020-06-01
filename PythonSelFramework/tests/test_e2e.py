# to run in terminal use -- py.test --browser_name chrome

from PythonSelFramework.utilities.BaseClass import BaseClass
from PythonSelFramework.pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all shop items")
        products = checkoutpage.getCardTitle()

        for product in products:
            productName = product.text
            log.info(product.text)
            if productName == "Blackberry":
                checkoutpage.getAddCart().click()
        checkoutpage.getCheckOut().click()
        confirmpage=checkoutpage.getCheckoutConfirm()
        log.info("entering country name")
        confirmpage.getCountryName().send_keys("Ind")
        self.verifyLink("India")
        confirmpage.getCountryLink().click()
        confirmpage.getcheckBox().click()
        confirmpage.getSubmitBtn().click()
        SuccessText = confirmpage.getAlertMsg().text
        log.info(SuccessText)
        assert "Success! Thank you!" in SuccessText
