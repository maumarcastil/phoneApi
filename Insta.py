from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


class Bot():

    def __init__(self):
        self.Login("th3pr0gr4mm3r", "mau3653511")
        time.sleep(2)
        #self.follow_followers_by_username("specialday_bq")
        self.GetFollowers("playadoptme")

    def Login(self, username, password):

        # Local variables

        path = r"D:\MM\Python\phone-api\geckodriver.exe"
        options = Options()
        options.add_argument("--private")

        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",
                               "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1")

        #options.add_argument("--private", "--headlees")
        # init
        self.driver = webdriver.Firefox(
            firefox_options=options, firefox_profile=profile, executable_path=path)
        self.driver.get("https://www.instagram.com")
        self.driver.set_window_size(375, 812)

        # Compelte login
        time.sleep(5)

        self.pressClickXpath("//button[.='Entrar']")
        time.sleep(3)

        self.completeInputXpath("//input[@name='username']", username)
        self.completeInputXpath("//input[@name='password']", password)

        # Press button
        self.pressClickXpath("//button[.='Iniciar sesión']")
        time.sleep(3)


    def follow_followers_by_username(self, username):
        time.sleep(2)



    


    # General Functions

    def completeInputXpath(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def completeInputName(self, name, value):
        self.driver.find_element_by_name(name).send_keys(value)

    def completeInputSelector(self, selector, value):
        self.driver.find_element_by_css_selector(selector).send_keys(value)

    def getInfoXpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath).get_attribute("href")

    def pressClickXpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def search(self, value):
        self.completeInputXpath("//input[@placeholder='Busca']", value)
        self.pressClickXpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")

    def GetFollowers(self, username):
        self.driver.get("https://www.instagram.com/" + username + "/")
        time.sleep(3)

        # Press followers
        self.pressClickXpath("/html/body/div[1]/section/main/div/ul/li[2]")

        time.sleep(30)
        array = [];
        for x in range(1,1000):
            print(self.getInfoXpath("/html/body/div[1]/section/main/div/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a".format(x)))

            #array.append(self.getInfoXpath("/html/body/div[1]/section/main/div/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a".format(x)))
        
        """ # See links
        for x in range(1,1000):
            print("{}:  {}".format(x, array[x]))
         """

def Main():
    MyBot = Bot()


if __name__ == "__main__":
    Main()


""" for (var i = 1; i <= 938; i++) {
   console.log(i +": " +arraycosas2[i]["href"])
} """

""" var arraycosas2 = [];
        for (var i = 1; i <= 999; i++) {
        arraycosas2.push(document.evaluate("/html/body/div[1]/section/main/div/ul/div/li["+ i +"]/div/div[1]/div[2]/div[1]/a", document.body, null, 9, null).singleNodeValue);
    } """


# print("//////////// ####  //////////// #### ////////////")

    # print("Ingresar usuario de INSTAGRAM")
    # usuario = input("->")
    # print("Ingresar contraseña de INSTAGRAM")
    # password = input("->")

    # driver.close()
