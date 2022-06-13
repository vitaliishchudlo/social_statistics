import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.headless = False
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def twitter(self, user, url=None):
        following_classname = 'css-901oao.css-16my406.r-18jsvk2.r-poiln3.r-1b43r93.r-b88u0q.r-1cwl3u0.r-bcqeeo.r-qvutc0'
        followers_classname = 'css-901oao.css-16my406.r-18jsvk2.r-poiln3.r-1b43r93.r-b88u0q.r-1cwl3u0.r-bcqeeo.r-qvutc0'
        username_xpath = 'css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0'
        response = {}
        if not url:
            user = f'https://twitter.com/{user}'
        self.driver.get(user)
        time.sleep(2)
        for x in range(15):
            try:
                stats = self.driver.find_elements(By.CLASS_NAME, 'css-4rbku5.css-18t94o4.css-901oao.r-18jsvk2.r-1loqt21.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0')
                for stat in stats:
                    if 'Following' in stat.text:
                        response['following'] = stat.text
                    if 'Followers' in stat.text:
                        response['followers'] = stat.text
            except Exception:
                time.sleep(0.1)
        return response

    def tiktok(self, user, url=None):
        following_xpath = '//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[1]/strong'
        followers_xpath = '//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong'
        username_xpath = '//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h2'
        response = {}
        if not url:
            user = f'https://www.tiktok.com/@{user}'
        self.driver.get(user)
        time.sleep(2)
        for x in range(15):
            try:
                response['following'] = self.driver.find_element(By.XPATH, following_xpath).text
                response['followers'] = self.driver.find_element(By.XPATH, followers_xpath).text
            except Exception:
                time.sleep(0.1)
        return response

