from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    countryName = (By.ID, "country")
    countryLink = (By.LINK_TEXT,'India')
    checkBox= (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitBtn = (By.CSS_SELECTOR,"[type='submit']")
    alertMsg = (By.CLASS_NAME, "alert-success")

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def getCountryLink(self):
        return self.driver.find_element(*ConfirmPage.countryLink)

    def getcheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmitBtn(self):
        return self.driver.find_element(*ConfirmPage.submitBtn)

    def getAlertMsg(self):
        return self.driver.find_element(*ConfirmPage.alertMsg)




