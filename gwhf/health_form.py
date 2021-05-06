from selenium import webdriver


class WebDriver():

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument("-incognito")
        # option.add_argument("--headless")
        # option.add_argument("disable-gpu")

        self.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=option)

if __name__ == '__main__':
    browser = WebDriver().browser
    print(browser)