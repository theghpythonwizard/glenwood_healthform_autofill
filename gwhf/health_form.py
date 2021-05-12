from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time


class WebDriver():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.headless = True
        # chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("-incognito")
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument("disable-infobars"); # disabling infobars
        # chrome_options.add_argument("--disable-extensions"); # disabling extensions

        self.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    def tear_down(self):
        self.browser.quit()

    def get_form(self, form_url):
        return self.browser.get(form_url)

    def set_fields(self, form_url):
        self.browser.get(form_url)
        text_boxes = self.browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
        submit_button = self.browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")

        text_boxes[0].send_keys("Miles")
        self.browser.implicitly_wait(3)
        submit_button[0].click()

        self.tear_down()


if __name__ == '__main__':
    runner = WebDriver()
    start = time.time()
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLScwakTS03jhKDx13ct0IEcp5szzxRGX-b6MlbSsJtfpxnu68A/viewform?usp=sf_link"
    end = time.time()
    execution_time = start - end
    print(execution_time)
    # form = runner.get_form(form_url)
    # print(form)
    textbox = runner.set_fields(form_url)
    # print(textbox)

