import requests
import json
import time
import subprocess
import regex
from requests.exceptions import HTTPError
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
def userConfigFile():
    try:
        with open('./Config.json', 'r') as f:
            creds = json.load(f)
            time.sleep(1)
        return creds['Username'], creds['Password']

    except FileNotFoundError:
        username = input("Enter Your Username:-")
        password = input("Enter Your Password:-")
        creds = {'Username': username, 'Password': password}
        with open('./Config.json', 'w') as f:

            json.dump(creds, f)
        print("Creating Config File..Done..Now Connecting it.")
        return username,password
def logoutNetwork():
    data = {
        'mode': '193',
        'username': 'singhrc',
        # 'a': '1700483046155',
        'producttype': '0',
    }


    response = requests.post('http://172.16.177.5:8090/logout.xml',
                         headers=headers, data=data, verify=False)
def loginNetwork(username,password):
    data = {
        'mode': '191',
        'username': username,
        'password': password,
        'producttype': '0',
    }

    print("Trying to log You In...")
    response = requests.post('http://172.16.177.5:8090/login.xml',
                            headers=headers, data=data, verify=False)
    if b'Invalid' in response.content.split():
       print("Incorrect Username and password.")
    else:
        print("Connected Succesfully.......Enjoy :)")
print('''
__      __  _    __   _                                          _
\ \    / / (_)  / _| (_)     __   ___   _ _    _ _    ___   __  | |_
 \ \/\/ /  | | |  _| | |    / _| / _ \ | ' \  | ' \  / -_) / _| |  _|
  \_/\_/   |_| |_|   |_|  __\__| \___/ |_||_| |_||_| \___| \__|  \__|
                         |___|
''')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
try:
    logoutNetwork()
except ConnectionError:

    print(subprocess.getoutput('netsh wlan connect RCOEM-BH-5G'))


username,password=userConfigFile()
loginNetwork(username=username,password=password)
time.sleep(3)

