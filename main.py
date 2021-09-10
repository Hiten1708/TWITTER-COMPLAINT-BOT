import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/hitenpatel/Driver/chromedriver"
TWITTER_EMAIL = ""
TWITTER_PASS = ""
spd_test_site = "https://www.speedtest.net"
twr_site = "https://twitter.com/HitenPatel1708"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = PROMISED_UP
        self.DOWN = PROMISED_DOWN
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        self.driver.get(spd_test_site)
        time.sleep(2)
        start_btn = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_btn.click()

        try:
            time.sleep(45)
            x = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
            x.click()
        except selenium.common.exceptions.NoSuchElementException:
            d_spd = float(self.driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
            u_spd = float(self.driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
            return [d_spd, u_spd]

        else:
            d_spd = float(self.driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
            u_spd = float(self.driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
            return [d_spd, u_spd]

    def tweet_at_provider(self, down, up):
        time.sleep(2)
        self.driver.get(twr_site)
        time.sleep(2)

        log_in = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/a')
        log_in.click()
        time.sleep(1)

        mail = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        mail.send_keys(TWITTER_EMAIL)

        pswd = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pswd.send_keys(TWITTER_PASS)
        pswd.send_keys(Keys.ENTER)

        self.driver.get('https://twitter.com/compose/tweet')

        time.sleep(3)

        twt_in = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        twt_in.send_keys(f'Bot Testing Alert! Please ignore \n internet speed: download: {down}/ upload: {up} and the promised speed is {PROMISED_DOWN}/{PROMISED_UP}')

        time.sleep(1)
        twt_in.send_keys(Keys.COMMAND, Keys.RETURN)


complain_bot = InternetSpeedTwitterBot()
int_lst = complain_bot.get_internet_speed()
if int_lst[0] > PROMISED_DOWN or int_lst[1] > PROMISED_UP:
    complain_bot.tweet_at_provider(int_lst[0], int_lst[1])
