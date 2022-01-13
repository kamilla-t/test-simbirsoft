class Calculator:

    def Base(self):
        locator = "//div[@class='card-section']"
        calculator = self.driver.find_element_by_xpath(locator)
        return calculator

    def Button(self, text):
        locator = "//div[@role='button' and text()='" + text + "']"
        button = self.Base().find_element_by_xpath(locator)
        return button

    def ClickButton(self, text):
        self.Button(text).click()

    def History(self):
        locator = "//span[@class='vUGUtc']"
        history = self.Base().find_element_by_xpath(locator)
        return history

        
    def Result(self):
        locator = "//span[@id='cwos']"
        result = self.Base().find_element_by_xpath(locator)
        return result

    def __init__(self, driver):
        self.driver = driver
        