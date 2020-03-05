# encoding:utf-8
import requests
App_id=17363741
APIkey="tAdrW89HdlWt1oG59xGTQ4V1"
SecretKey="6nt07LPLynaa2qLUGai6mtpDj7USnYkB"

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+APIkey+'&client_secret='+SecretKey
response = requests.get(host)
if response:
    print(response.json())