from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json


class Dispositivo(object):
    def __init__(self, name, brand, img):
        self.name = name
        self.brand = brand
        self.img = img

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Bot():
    def __init__(self):
        path = r"D:\MAURICIO\phoneApi\geckodriver.exe"
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

    def get_all_devices_for_brands(self):
        i = 0
        links_brands = list(self.browser.execute_script(
            "return [...document.querySelectorAll('.navigation-list li.item')].map(x => x.lastChild.lastChild.href)"))
        for x in links_brands:
            ##print("Ingresando a una nueva marca")
            self.browser.get(x)
            time.sleep(3)

            # Get data(NameBrand)
            name_brand = self.browser.execute_script(
                "return document.querySelector('.h-main .h-right h1').innerText")
            name_brand = name_brand.replace(
                "Comparar precios de móviles libres de ", "")

            # Get url of all devices
            links_devices = list(self.browser.execute_script(
                "return [...document.querySelectorAll('.item.smartphone a')].map(x => x.href)"))
            for y in links_devices:
                ##print("Ingresando a un nuevo dispositivo")
                self.browser.get(y)
                time.sleep(2)

                # Get nameDevice and imgs
                imgs_device = self.browser.execute_script(
                    "return [...document.querySelectorAll('a.kigallery')].map(x => x.href.search('cdn-files.kimovil.com') != -1 ? x.href : false)")
                name_device = self.browser.execute_script(
                    "return document.querySelector('.wrapper .title-group h1').lastChild.wholeText.trim()")

                # Created Device
                device = Dispositivo(name_device, name_brand, imgs_device)

                print("Mostrando dispositivo")
                print(device.to_JSON())

        i = i + 1


def Main():
    MyBot = Bot()
    MyBot.get_all_devices_for_brands()
    print("Finalizo")


if __name__ == '__main__':
    Main()
