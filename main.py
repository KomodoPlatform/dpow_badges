import badge_lib


def main():
    while True:
        badge_lib.update_last_nota_status(badge_lib.kmd_notarized_coins)
        for coin_data in badge_lib.kmd_notarized_coins:
            badge_lib.create_coin_badge(coin_data)
        # TODO: just add sleep there to re-draw badges periodically
        break


if __name__ == '__main__':
    main()
