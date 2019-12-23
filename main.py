import badge_lib
import time
from coins_list import kmd_notarized_coins

def main():
    while True:
        badge_lib.coin_dpow_badge(kmd_notarized_coins)
        time.sleep(360)


if __name__ == '__main__':
    main()
