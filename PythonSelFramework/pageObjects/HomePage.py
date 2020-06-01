from selenium.webdriver.common.by import By
from PythonSelFramework.pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME,"email")
    password = (By.CSS_SELECTOR,"[type='password']")
    checkBox = (By.ID,"exampleCheck1")
    dropDown = (By.ID,"exampleFormControlSelect1")
    submit = (By.XPATH,"//input[@type='submit']")
    alertMsg = (By.CLASS_NAME,"alert-success")
    shop = (By.CSS_SELECTOR,"a[href*='shop']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getDropDown(self):
        return self.driver.find_element(*HomePage.dropDown)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alertMsg)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        # self.driver.
