import requests
import time
import json
import sys
from PIL import Image, ImageDraw, ImageFont


kmd_notarized_coins = [
    {
        "name": "KMD",
        "version": "0.5.0",
        "status": "active",
        "network": "main",
        "minutes_since_nota": ""
    },
    {
        "name": "AXO",
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