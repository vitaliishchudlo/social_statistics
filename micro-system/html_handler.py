from config import *

def response_choose_network(available_networks):
    networks_html = ''
    for network in available_networks:
        networks_html += f'<p><input type="radio" name="ssid" value="{network}" id="{network}"><label for="{network}">&nbsp;{network}</label></p>'
    response = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <title>WiFi Manager</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html, body {
            display: table;
            margin: auto;
        }
    </style>
</head>
<h1>Wi-Fi Manager</h1>
<form action="/configure" method="POST" accept-charset="utf-8"> """ + networks_html + """
    <p><label for="password">Password:&nbsp;</label><input type="password" id="password" name="password"></p>
    <p><input type="submit" value="Connect"></p>
</form>
</body>
</html>
<body>
"""
    return response

def bad_wifi_credentials(ssid, error):
    response = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>WiFi Manager</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html, body {
            display: table;
            margin: auto;
        }
    </style>
</head>
<body> """ + f'<h1>{ssid}</h1>' + f'<h3>{error}</h3>' + """ 
<form action="/" method="POST">
    <button type="submit">Return back</button>
</form>
</body>
</html>
"""
    return response


def html_conf_webserver():
    targets = read_config_file()['targets']
    table = ''
    if targets:
        for target in targets.items():
            print(target[0] + "tar0")
            print(target[1] + "tar1")
            table += '<tr><td>&nbsp<b>' + target[0] + '</b></td>' + \
            '<td>&nbsp' + target[1] + '</td></tr>'
    response = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        html {
            font-family: Arial;
            font-size: 20px;
            display: inline-block;
            margin: 1px auto;
            text-align: center;
            background-color: #cdcdc9;
        }

        h1 {
            font-size: 35px;
            color: #0F3376;
            padding: 2vh;
        }

        h3 {
            font-size: 25px;
            color: red;
        }

        table {
            font-size: 20px;
        }

        .status_table {
            font-size: 1.3rem;
        }

        table {
            margin: 0 auto; /* or margin: 0 auto 0 auto */
        }

        .error {
            color: red;
            font-size: 18px;
        }

        .button_submit {
            padding: 15px 25px;
            font-size: 18px;
            text-align: center;
            cursor: pointer;
            outline: none;
            color: #fff;
            background-color: #04AA6D;
            border: none;
            border-radius: 15px;
            box-shadow: 0 6px rgb(13, 75, 11);
        }

        .button_submit:hover {
            background-color: #3e8e41
        }

        .button_submit:active {
            background-color: #3e8e41;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }
    </style>
</head>
<body>
<div class="title" style="text-align: center;">
    <h1>Configuration page</h1>
    <hr width="900" size="2" color="#00000"/>
</div>
<div class="status_table" style="text-align: center;">
    <h3> Already activated: </h3>
    <table style="width: 2%;" border="3">
        <tbody> """ + table + """ </tbody>
    </table>    
</div>
<div class="main" style="text-align: center; padding: 15px;">
    <form>
        <div class="choices">
            <input type="radio" id="choice1" name="target" value="twitter">
            <label for="choice1">Twitter</label>
            <input type="radio" id="choice2" name="target" value="tiktok">
            <label for="choice2">TikTok</label>
            <input type="radio" id="choice3" name="target" value="youtube">
            <label for="choice3">YouTube</label>
        </div>
        <div class="input_field">
            <p>Link: <input name="link"></p>
        </div>
        <p class="error"><b></b></p>
        <div class="submit_form">
            <button class="button_submit" type="submit" id="btn1">Save</button>
        </div>
    </form>
</div>
</body>
</html>

"""
    return response
    
    
    
    

    
    
