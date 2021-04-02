from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class Scraper():
    def __init__(self, url=""):
        # placeholders
        self.pair = ""
        self.currency1_amount = -1
        self.reverse = False


        # LOAD Site
        option = webdriver.ChromeOptions()

        self.browser = webdriver.Chrome(executable_path="./drivers/chromedriver", chrome_options=option)
        self.browser.get(url)
        self.browser.implicitly_wait(5)
        # Find elements
        # Buttons
        self.currency_1_btn = self.browser.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[2]/button')
        self.currency_2_btn = self.browser.find_element_by_xpath('//*[@id="swap-currency-output"]/div/div[2]/button')
        # Input
        self.currency_1_input = self.browser.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[2]/input')
        self.currency_2_input = self.browser.find_element_by_xpath('//*[@id="swap-currency-output"]/div/div[2]/input')

    # HELPER FUNCTIONS #

    # Add currency 1 value that we want to convert (by default this will be 1
    def send_currency_1_amount(self, amount=1):
        self.currency_1_input.click()
        self.currency_1_input.send_keys(str(amount))

    def send_currency_2_amount(self, amount=1):
        self.currency_2_input.click()
        self.currency_2_input.send_keys(str(amount))

    def select_pair(self, currency1="BNB", currency2="BUSD", reverse=False, currency1_amount=1 ):
        self.reverse = reverse
        # Select first currency
        self.currency_1_btn.click()
        token_search = self.browser.find_element_by_id("token-search-input")
        token_search.send_keys(currency1)
        self.browser.implicitly_wait(3)
        token_search.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(1)

        # select second currency
        self.currency_2_btn.click()
        token_search = self.browser.find_element_by_id("token-search-input")
        token_search.send_keys(currency2)
        self.browser.implicitly_wait(1)
        token_search.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(1)
        # only send currency value if its changing
        if self.pair == "" or currency1_amount != self.currency1_amount:
            if reverse:
                self.send_currency_2_amount(amount=currency1_amount)
                self.currency1_amount = currency1_amount
            else:
                self.send_currency_1_amount(amount=currency1_amount)
                self.currency1_amount = currency1_amount
        # create pair, to be used for return
        self.pair = str(currency1) + "/" + str(currency2)

    # pancakeswap updates every 30 seconds, you can call this in a loop for continuous collection
    def get_pair_price(self):
        # print(self.reverse)
        # wait for input value to update, create loop to get updated value
        if self.reverse:
            value = self.currency_1_input.get_attribute("value")
            while value is None or value == "":
                value = self.currency_1_input.get_attribute("value")
        else:
            value = self.currency_2_input.get_attribute("value")
            while value is None or value == "":
                value = self.currency_2_input.get_attribute("value")


        # returns two values, first one is saved to database (save_data == data),
        # second one is used for determining correct path

        date_data = datetime.now()
        return {"time": date_data.strftime("%m/%d/%Y, %H:%M:%S"), "value": value, "pair": self.pair.replace('/', '_')}












