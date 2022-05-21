from flask import Flask, request, jsonify

app = Flask(__name__)

LINK_PREFIX = 'api_v1/social_statistics'
AVAILABLE_PLATFORMS = ['instagram', 'twitter']


@app.route('/')
def index():
    return 'Are you sure ?'


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

    return 'Text'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
