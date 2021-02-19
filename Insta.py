from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


class Bot():

    def __init__(self):
        self.init_browser()
        time.sleep(2)

    def init_browser(self):
        path = r"D:\MAURICIO\phoneApi\geckodriver.exe"
        options = Options()
        options.add_argument("--private")

        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",
                               "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1")
        driver = webdriver.Firefox(
            firefox_options=options, firefox_profile=profile, executable_path=path)

        driver.get("https://www.kimovil.com/es/todas-las-marcas-de-moviles")
        
        time.sleep(5)
        
        marca = driver.execute_script("return [...document.querySelectorAll('.navigation-list li.item')].map(x => x.lastChild.lastChild.querySelector('.info').querySelector('.title').innerText )")
        print(marca)

def Main():
    MyBot = Bot()


if __name__ == "__main__":
    Main()


# document.querySelectorAll("li figure a.kigallery").forEach(x => console.log(x.href))
    
    ##document.querySelectorAll(".navigation-list li.item").forEach(x =>{ console.log(x.lastChild.lastChild.querySelector(".info").querySelector(".title").innerText ) })
    
    ##document.querySelectorAll(".navigation-list li.item").forEach(x =>{ console.log(x.lastChild.lastChild.querySelector(".image").querySelector("img").src ) })
