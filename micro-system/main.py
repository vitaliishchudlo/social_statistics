import ntptime
import time
import _thread
import sys
import urequests
from config import *
from statuses import *

print(str(wlan_status) + str(lcd_status))
#if not wlan_status or not lcd_status:
#    sys.exit()
    

def show_config_tip(wlan_ip):
    lcd.clear()
    lcd.puts(' ' + str(wlan_ip), 0, 1)
    for x in range(7):
        lcd.puts('_ _ Settings_ _ ', 0, 0)
        time.sleep(0.8)
        lcd.puts('                ', 0, 0)
        

def show_time():
    for x in range(3):
        now = time.localtime()
        lcd.puts('   ' + str(now[2]) + '.' + str(now[1]) + '.' + str(now[0]) , 0, 0)
        lcd.puts('   ' + str(now[3]) + ':' + str(now[4]) + ':' + str(now[5]) , 0, 1)
        time.sleep(1)




def display_process():
    while True:
        try:
            
            # twitter
            try:
                lcd.clear()
                config_json = read_config_file()
                link = config_json['targets']['twitter']
                lcd.puts('Twitter')
                builded_link = 'http://192.168.0.105:5000/api_v1/get_social_data/' \
                               + '?' + 'platform=twitter' + '&username=' + link
                print(builded_link)
                request = urequests.get(builded_link)
                response = json.loads(request.text)
                try:
                    lcd.puts('Followers:' + str(response['followers']), 0, 0)
                    lcd.puts('Following:' + str(response['following']), 0, 1)
                except KeyError:
                    lcd.puts(str(response['error']), 0, 1)
                print('sleeping 10 after Twitter')
                time.sleep(3)
            except KeyError:
                pass
            
            # tiktok
            try:
                lcd.clear()
                config_json = read_config_file()
                link = config_json['targets']['tiktok']
                lcd.puts('TikTok')
                builded_link = 'http://192.168.0.105:5000/api_v1/get_social_data/' \
                               + '?' + 'platform=tiktok' + '&username=' + link
                print(builded_link)
                request = urequests.get(builded_link)
                response = json.loads(request.text)
                try:
                    lcd.puts('Followers:' + str(response['followers']), 0, 0)
                    lcd.puts('Following:' + str(response['following']), 0, 1)
                except KeyError:
                    lcd.puts(str(response['error']), 0, 1)
                print('sleeping 10 after TikTok')
                time.sleep(3)
            except KeyError:
                pass

            # youtube
            try:
                lcd.clear()
                config_json = read_config_file()
                link = config_json['targets']['youtube']
                lcd.puts('Youtube')
                builded_link = 'http://192.168.0.105:5000/api_v1/get_social_data/' \
                               + '?' + 'platform=youtube' + '&username=' + link
                print(builded_link)
                request = urequests.get(builded_link)
                response = json.loads(request.text)
                try:
                    lcd.puts('Followers:' + str(response['followers']), 0, 0)
                except KeyError:
                    lcd.puts(str(response['error']), 0, 1)
                print('sleeping 10 after Youtube')
                time.sleep(3)
            except KeyError:
                pass
            
            lcd.clear()
            show_time()

        except OSError as err:
            # LCD - 116 | Network - -202
            if err.value == 116:
                lcd_error_pin.on()
                lcd_status = False
                print('LCD Broken!')
            if err.value == -202:
                network_error_pin.on()
                wlan_status = False
                print('Network broken!')
            
            

    

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
            

    conf_webserver.run(host=wlan_ip,port=80)
       
    

    
print(wlan.ifconfig()[0])

if __name__ == '__main__':
    #show_config_tip(wlan_ip)
    display_thread = _thread.start_new_thread(display_process, ())
    configurationWebServer()
    