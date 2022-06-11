import time
import _thread
import urequests
from config import *


def show_config_tip(wlan_ip):
    lcd.clear()
    lcd.puts(' ' + str(wlan_ip), 0, 1)
    for x in range(7):
        lcd.puts('_ _ Settings_ _ ', 0, 0)
        time.sleep(0.8)
        lcd.puts('                ', 0, 0)


def display_process():
    while True:
        try:
            # instagram
            try:
                lcd.clear()
                config_json = read_config_file()
                link = config_json['targets']['instagram']
                lcd.puts('Instagram')
                builded_link = 'http://34.207.67.56:8080/api_v1/get_data/' \
                               + '?' + 'platform=instagram' + '&username=' + link
                request = urequests.get(builded_link)
                response = json.loads(request.text)
                lcd.puts('Followers:' + str(response['followers']), 0, 0)
                lcd.puts('Following:' + str(response['following']), 0, 1)
                print('sleeping 10 after instagram')
                time.sleep(10)
            except KeyError:
                pass

            # twitter
            try:
                lcd.clear()
                config_json = read_config_file()
                link = config_json['targets']['twitter']
                lcd.puts('Twitter')
                builded_link = 'http://34.207.67.56:8080/api_v1/get_data/' \
                               + '?' + 'platform=instagram' + '&username=' + link
                request = urequests.get(builded_link)
                response = json.loads(request.text)
                lcd.puts('Followers:' + str(response['followers']), 0, 0)
                lcd.puts('Following:' + str(response['following']), 0, 1)
                print('sleeping 10 after Twitter')
                time.sleep(10)
            except KeyError:
                pass

            # tiktok
            # try:
            #   config_json = read_config_file()['targets']
            #    link = config_json['tiktok']
            # except KeyError:
            #    pass

            # youtube
            # try:
            #    config_json = read_config_file()['targets']
            #    link = config_json['youtube']
            # except KeyError:
            #    pass
        except OSError as err:
            # LCD - 116 | Network - -202
            if err.value == 116:
                lcd_error_pin.on()
                lcd_status = False
                print('LCD Broken')
            if err.value == -202:
                network_error_pin.on()
                wlan_status = False
                print('Network broken')
        finally:
            print('AGAIN')
            time.sleep(3)


def configurationWebServer():
    conf_webserver = Microdot()

    @conf_webserver.route('/', methods=["GET", "POST"])
    async def index(request):
        if not request.args:
            return Response(body=html_conf_webserver(), headers={"Content-Type": "text/html"})

        try:
            link = request.args['link']
        except Exception:
            link = None
        try:
            target = request.args['target']
        except Exception:
            target = None

        if target and not link:
            delete_target(target=target)

        if target and link:
            write_target(target=target, link=link)

        return Response(body=html_conf_webserver(), headers={"Content-Type": "text/html"})

    conf_webserver.run(host=wlan_ip, port=80)


print(wlan.ifconfig()[0])

if __name__ == '__main__':
    # show_config_tip(wlan_ip)
    display_thread = _thread.start_new_thread(display_process, ())
    configurationWebServer()

