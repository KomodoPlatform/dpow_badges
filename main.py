import badge_lib
import time


def main():
    while True:
        badge_lib.coin_dpow_badge(badge_lib.kmd_notarized_coins)
        time.sleep(360)


if __name__ == '__main__':
    main()
