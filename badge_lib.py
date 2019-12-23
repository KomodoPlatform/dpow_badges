import requests
import time
import json
import sys
from PIL import Image, ImageDraw, ImageFont
from pybadges import badge

kmd_notarized_coins = [
    {
        "name": "AXO",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "BET",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "BNTN",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "BOTS",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "BTCH",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "CCL",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "CEAL",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "CHAIN",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "CHIPS",
        "version": "dev",
        "status": "active",
        "network": "3rd party",
        "minutes_since_nota": ""
    },
    {
        "name": "COMMOD",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "COQUICASH",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "CRYPTO",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "DEX",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "DION",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "DSEC",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "EMC2",
        "version": "latest master",
        "status": "active",
        "network": "3rd party",
        "minutes_since_nota": ""
    },
    {
        "name": "EQL",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "ETOMIC",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "GAME",
        "version": "latest master",
        "status": "active",
        "network": "3rd party",
        "minutes_since_nota": ""
    },
    {
        "name": "GIN",
        "version": "latest master",
        "status": "active",
        "network": "3rd party",
        "minutes_since_nota": ""
    },
    {
        "name": "HODL",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "HUSH3",
        "version": "0.4.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "ILN",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "JUMBLR",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "K64",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "KMD",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "KMDICE",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "KOIN",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "KSB",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "KV",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "MESH",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "MGW",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "MORTY",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "MSHARK",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "NINJA",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "OOT",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "OUR",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "PANGEA",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "PGT",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "PIRATE",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "PRLPAY",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "REVS",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "RFOX",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "RICK",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "SEC",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "SUPERNET",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "THC",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "VRSC",
        "version": "n/a",
        "status": "disabled",
        "network": "3rd party",
        "minutes_since_nota": ""
    },
    {
        "name": "WLC",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "WLC21",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "ZEXO",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "ZILLA",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    }
]


def update_last_nota_status(notarized_coins_list):
    for coin in notarized_coins_list:
        coin_status_dict = json.loads(requests.get("https://komodostats.com/api/notary/coin.json",
                                                   params={"coinName": coin["name"]}).content)
        minutes_since_last_nota = (int(time.time()) - coin_status_dict["lastnotarization"]) / 60
        coin["minutes_since_nota"] = round(minutes_since_last_nota)


def create_coin_badge(coin_data):

    badge_image = Image.new("RGBA", (240, 240), color=0)
    coin_logo = Image.open(sys.path[0]+"/icons/"+coin_data["name"]+".png")

    badge_font = ImageFont.truetype('Roboto-Regular.ttf', 20)

    d = ImageDraw.Draw(badge_image)

    d.text((10, badge_image.size[1]/4), "Name: " + coin_data["name"], font=badge_font, fill="#000000")
    d.text((10, badge_image.size[1]/4 + 25), "Version: " + coin_data["version"], font=badge_font, fill="#000000")
    d.text((10, badge_image.size[1]/4 + 50), "Status: " + coin_data["status"], font=badge_font, fill="#000000")
    d.text((10, badge_image.size[1]/4 + 75), "Network: " + coin_data["network"], font=badge_font, fill="#000000")
    d.text((10, badge_image.size[1]/4 + 100), "Last nota: " + str(coin_data["minutes_since_nota"]) + " min. ago", font=badge_font, fill="#000000")

    (width1, height1) = coin_logo.size
    (width2, height2) = badge_image.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGBA', (result_width, result_height))
    result.paste(im=badge_image, box=(0, 0))
    result.paste(im=coin_logo, box=(width1, 0))

    result.save(coin_data["name"]+"_badge.png")


def coin_dpow_badge(notarized_coins_list):
    coins_notarization_info = json.loads(requests.get("https://komodostats.com/api/notary/summary.json").content)
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
               if int(coin_data["minutes_since_nota"]) < 144:
                   coin_dpow_status = "active"
                   status_color = "green"
               elif 720 < int(coin_data["minutes_since_nota"]) < 1440:
                   coin_dpow_status = "irregular"
                   status_color = "yellow"
               else:
                   coin_dpow_status = "inactive"
                   status_color = "red"
               dpow_status_badge = badge(left_text='dPOW status', right_text=coin_dpow_status, right_color=status_color)
               with open("/var/www/html/svg/"+coin_data["name"]+"_badge.svg", 'w') as f:
                   f.write(dpow_status_badge)

