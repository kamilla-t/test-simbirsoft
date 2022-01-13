from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.Calculator import Calculator
from pages.SearchPage import SearchPage

class App:

    def __init__(self):
        driver_path = "./drivers/chromedriver.exe"
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(driver_path, options=options)

        self.driver.get("https://www.google.com/")

    def Calculator(self):
        return Calculator(self.driver)

    def SearchPage(self):
        return SearchPage(self.driver)