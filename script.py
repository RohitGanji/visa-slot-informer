import requests
from datetime import datetime
import time

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
headers = {
    'User-Agent': USER_AGENT,
    'Cookie': '<account-cookie>' # login into your account and extract the cookie using the chrome developer tools.
}

def telegram(message):
    token = '<telegram_bot_token>'
    chat_id = '<account_chat_id>'
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=HTML')

while True:
    visa = requests.get('https://cgifederal.secure.force.com/scheduleappointment', headers=headers)
    if (visa.text.find('HYDERABAD') > 0) and (visa.text.find('There are currently no appointments available.') < 0): # Change the city from HYDERABAD to your city
        telegram(datetime.now().strftime("%H:%M:%S")+" - Slot Available!")
    else:
        print(datetime.now().strftime("%H:%M:%S")+" - Slot Not Available")
    time.sleep(15)
