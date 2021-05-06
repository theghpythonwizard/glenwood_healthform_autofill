from selenium import webdriver


class WebDriver():

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument("-incognito")
        option.add_argument("--headless")
        option.add_argument("disable-gpu")

        self.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=option)

    def get_form(self, form_url):
        return self.browser.get(form_url)

    def set_fields(self, form_url):
        self.browser.get(form_url)
        text_boxes = self.browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
        submit_button = self.browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")

        text_boxes[0].send_keys("Miles")
        submit_button[0].click()

        self.browser.close()


if __name__ == '__main__':
    runner = WebDriver()
    textbox = runner.set_fields("https://docs.google.com/forms/d/e/1FAIpQLScwakTS03jhKDx13ct0IEcp5szzxRGX-b6MlbSsJtfpxnu68A/viewform?usp=sf_link")
    # print(textbox)

