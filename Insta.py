from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


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

    def init_browser(self):
        self.browser.get("https://www.kimovil.com/es/todas-las-marcas-de-moviles")

        time.sleep(5)

    

        marca = driver.execute_script(
            "return [...document.querySelectorAll('.navigation-list li.item')].map(x => x.lastChild.lastChild.querySelector('.info').querySelector('.title').innerText )")
        print(marca)


def Main():
    MyBot = Bot()


if __name__ == "__main__":
    Main()

##galeria
# document.querySelectorAll("li figure a.kigallery").forEach(x => console.log(x.href))

##Marcas
# document.querySelectorAll(".navigation-list li.item").forEach(x =>{ console.log(x.lastChild.lastChild.querySelector(".info").querySelector(".title").innerText ) })
# document.querySelectorAll(".navigation-list li.item").forEach(x =>{ console.log(x.lastChild.lastChild.querySelector(".image").querySelector("img").src ) })