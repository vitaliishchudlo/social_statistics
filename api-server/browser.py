import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self):
        # chromedriver_autoinstaller.install()

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        service = Service(ChromeDriverManager().install())
        options.headless = False
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.delete_all_cookies()

    def twitter(self, user, url=None):
        following_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[5]/div[1]/a/span[1]/span'
        followers_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[5]/div[2]/a/span[1]/span'
        username_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/span'
        response = {}
        if not url:
            user = f'https://twitter.com/{user}'
        self.driver.get(user)
        time.sleep(2)
        for x in range(20):
            try:
                print(x)
                response['following'] = self.driver.find_element(By.XPATH, following_xpath).text
                response['followers'] = self.driver.find_element(By.XPATH, followers_xpath).text
            except Exception:
                time.sleep(0.1)
        return {'followers': followers, 'following': following}

# def get_instagram_stats(username):
#     import ipdb;
#     ipdb.set_trace(context=5)
#
#     login_input_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
#     password_input_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
#     login_button_xpath = '//*[@id="loginForm"]/div/div[3]/button'
#
#     driver.get(username)
#
#     login_input = driver.find_element(By.XPATH, login_input_xpath)
#     password_input = driver.find_element(By.XPATH, password_input_xpath)
#     login_button = driver.find_element(By.XPATH, login_button_xpath)
#     driver.find_element(By.XPATH, '')
