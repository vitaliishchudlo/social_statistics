import json
import time


def read_config_file():
    try:
        with open('config.json', 'r') as file:
            config = file.read()
            config_json = json.loads(config)
        return config_json
    except Exception:
        raise


def write_network(ssid, password):
    try:
        config_json = read_config_file()
        config_json['network']['ssid'] = ssid
        config_json['network']['password'] = password
        with open('config.json', 'w') as file:
            file.write(json.dumps(config_json))
        return True
    except Exception:
        raise


def delete_network():
    try:
        config_json = read_config_file()
        config_json['network']['ssid'] = None
        config_json['network']['password'] = None
        with open('config.json', 'w') as file:
            file.write(json.dumps(config_json))
        return True
    except Exception:
        raise
