from selenium.webdriver.common.keys import Keys

class SearchPage:
    def SearchInput(self):
        locator = ".//input[@title='Поиск']"
        search_input = self.driver.find_element_by_xpath(locator)
        return search_input

    def Search(self, text):
        self.SearchInput().send_keys(text)
        self.SearchInput().send_keys(Keys.ENTER)

    def Submit(self):
        locatpr = ".//input[@value='Поиск в Google']"
        submit_button = self.driver.find_element_by_xpath(locatpr)
        return submit_button

    def __init__(self, driver):
        self.driver = driver
        