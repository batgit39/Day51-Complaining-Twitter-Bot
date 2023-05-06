import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 

PROMISED_DOWN = 50
PROMISED_UP = 50
# change this to your promiced speed
CHROME_DRIVER_PATH = ''
# add your driver path
TWITTER_EMAIL = "" 
TWITTER_PWD = ""
# add your details

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service('/home/mitresh/Development-Selenium/chromedriver'))
        # driver.maximize_window()
        self.up = ""
        self.down = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        while True:
            try:
                go_button.click()
            except:
                time.sleep(2)
            else:
                break

        time.sleep(30)
        while True:
            try:
                self.up = float(self.up)
                self.down = float(self.down)
            except: 
                self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
                self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            else:
                break

        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(15)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(5)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PWD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(60)
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(5)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

mrbot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
mrbot.get_internet_speed()
mrbot.tweet_at_provider()
