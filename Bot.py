from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json

import phone_api


class Bot():
    def __init__(self):
        path = r"D:\MM\Python\phoneApi\geckodriver.exe"
        options = Options()
        options.add_argument("--private")

        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",
                               "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1")
        self.browser = webdriver.Firefox(
            firefox_options=options, firefox_profile=profile, executable_path=path)

        self.browser.get(
            "https://www.kimovil.com/es/todas-las-marcas-de-moviles")

        time.sleep(2)
        print("Finalizo")

    def get_all_links_brands(self):
        links_brands = self.browser.execute_script(
            "return [...document.querySelectorAll('.navigation-list li.item')].map(x => x.lastChild.lastChild.href)")
        print(links_brands[0])


def Main():
    MyBot = Bot()
    MyBot.get_all_links_brands()


if __name__ == '__main__':
    Main()
