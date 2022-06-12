import chromedriver_autoinstaller
from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from flask import Flask, request, jsonify

# WebServer
app = Flask(__name__)

# ChromeWindow
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])
service = Service()
options.headless = False
driver = webdriver.Chrome(
    options=options, service=service)

LINK_PREFIX = 'api_v1/'
AVAILABLE_PLATFORMS = ['instagram', 'twitter', 'tiktok', 'youtube']


@app.route('/')
def index():
    return 'Are you sure ?'


def get_instagram_stats(username, url):
    driver.get('https://github.com/vitaliishchudlo/steam_name_changer/blob/production/app.py')


def get_twitter_stats(username):
    pass


@app.route(f'/{LINK_PREFIX}/get_social_data/')
def get_social_data():
    if not request.args.get('platform'):
        return jsonify(error="You must specify a 'platform' parameter in the link")
    if not str(request.args.get('platform')).lower() in AVAILABLE_PLATFORMS:
        return jsonify(error=f"Available platforms are: {', '.join(AVAILABLE_PLATFORMS)}")
    if not request.args.get('username'):
        return jsonify(error="You must specify a 'username' parameter in the link")
    if not len(request.args.get('username')) > 4:
        return jsonify(error='Your username is not true')

    platform = request.args.get('platform')
    username = request.args.get('username')

    if 'https://' in username:
        url = True
    else:
        url = False

    if platform == 'instagram':
        if url:
            if not bool('https://www.instagram.com/' in url):
                return jsonify(error='Bad url')
        response = get_instagram_stats(username, url)
        return jsonify(username=username,
                       platform=platform,
                       followers=response['followers'],
                       following=response['following'])


    elif platform == 'twitter':
        response = get_twitter_stats(username)
        return jsonify(username=username, platform=platform, followers=152, following=224)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
