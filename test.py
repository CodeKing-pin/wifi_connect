import requests
import json,time,subprocess
import pyfiglet
from termcolor import cprint
from requests.exceptions import HTTPError
cprint(pyfiglet.figlet_format("WIFI_CON", font='starwars'), attrs=['bold'])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
try:
    try:
        with open('./Config.json','r') as f:
            creds=json.load(f)
            time.sleep(1)
    except FileNotFoundError:
        username=input("Enter Your Username:-")
        password=input("Enter Your Password:-")
        creds={'Username':username,'Password':password}
        with open('./Config.json','w') as f:
        
            json.dump(creds,f)
        print("Creating Config File..Done..Now Connecting it.")
    out1=subprocess.getoutput('netsh wlan connect RCOEM-BH-5G')
    if 'successfully' not in  out1.split():print("Looks 'RCOEM-BH-5G' not available.")
    username=creds['Username']
    password = creds['Password']
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://172.16.177.5:8090',
        'Pragma': 'no-cache',
        'Referer': 'http://172.16.177.5:8090/httpclient.html',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    data = {
        'mode': '191',
        'username': username,
        'password': password,
        'producttype': '0',
    }
    try:
        print("Trying to log You In...")
        response = requests.post('http://172.16.177.5:8090/login.xml',
                                    headers=headers, data=data, verify=False)
        if b'Invalid' in response.content.split():
            print("Check Username and password")
        else:
            print("Connected Succesfully.......Enjoy :)")
    except HTTPError:
        print("1)Something Went Wrong")
    time.sleep(5)
except:
        print("Something Went Wrong")
        time.sleep(3)
