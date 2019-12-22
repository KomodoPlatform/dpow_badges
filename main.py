import badge_lib
import time


def main():
    while True:
        # badge_lib.update_last_nota_status(badge_lib.kmd_notarized_coins)
        for coin_data in badge_lib.kmd_notarized_coins:
            badge_lib.coin_dpow_badge(coin_data)
        time.sleep(360)


if __name__ == '__main__':
    main()
