import requests
import time
from datetime import datetime
import json
import sys
import pytz
from pybadges import badge


def coin_dpow_badge(notarized_coins_list):
    try:
        coins_notarization_info = json.loads(requests.get("https://komodostats.com/api/notary/summary.json").content)
    except Exception as e:
        print(e)
    print("Creating date badge")
    fetch_time = datetime.now(pytz.utc)
    fetch_time_string = fetch_time.strftime("%d/%m/%Y %H:%M:%S UTC")
    dpow_date_badge = badge(left_text='dPOW status', right_text="fetched at: " + fetch_time_string, right_color="black")
    with open("/var/www/html/svg/"+"date_badge.svg", 'w') as f:
        f.write(dpow_date_badge)
    for coin_data in notarized_coins_list:
        print("Creating badge for " + coin_data["name"])
        for coin_fetched_data in coins_notarization_info:
           if coin_data["name"] == coin_fetched_data["ac_name"]:
               try:
                   minutes_since_last_nota = (int(time.time()) - coin_fetched_data["lastnotarization"]) / 60
                   coin_data["minutes_since_nota"] = round(minutes_since_last_nota)
               except Exception as e:
                   print(e)
                   print(coin_data)
                   print(coin_fetched_data)
               else:
                   if int(coin_data["minutes_since_nota"]) < 144:
                       coin_dpow_status = "active"
                       status_color = "green"
                   elif int(coin_data["minutes_since_nota"]) < 1440:
                       coin_dpow_status = "irregular"
                       status_color = "yellow"
                   else:
                       coin_dpow_status = "inactive"
                       status_color = "red"
                   dpow_status_badge = badge(left_text='dPOW status', right_text=coin_dpow_status, right_color=status_color)
                   with open("/var/www/html/svg/"+coin_data["name"]+"_badge.svg", 'w') as f:
                       f.write(dpow_status_badge)

