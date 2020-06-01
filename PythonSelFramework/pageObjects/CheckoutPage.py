from selenium.webdriver.common.by import By
from PythonSelFramework.pageObjects.ConfirmPage import ConfirmPage



class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitles = (By.XPATH,"//div[@class='card h-100']/div/h4/a")

    addCart = (By.CSS_SELECTOR,"[class='btn btn-info']")
    CheckOut = (By.CSS_SELECTOR,"a[class*='btn btn-primary']")
    CheckoutTwice= (By.CSS_SELECTOR,"[class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getAddCart(self):
        return self.driver.find_element(*CheckoutPage.addCart)

    def getCheckOut(self):
        return self.driver.find_element(*CheckoutPage.CheckOut)

    def getCheckoutConfirm(self):
        self.driver.find_element(*CheckoutPage.CheckoutTwice).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
