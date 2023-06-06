
import webscrap as ws
import log
import os
import time


def main():
    retrys = 8
    for i in range(retrys):
        try:
            ws_str: str = ws.get_bitcoin_coinmarketcap()

            # write coinmarketcap log
            log.write_log(ws_str, "logs/test_log.txt")
            log.write_log(ws_str,"logs/coin_market_cap_log.txt")
            break
        except AttributeError as e:
            print("Error: {}\nretrying... {} / {}".format(e, i, retrys))
            time.sleep(8)

def test():
    retrys = 8
    for i in range(retrys):
        try:
            ws_str: str = ws.get_bitcoin_coinmarketcap()

            # write coinmarketcap log
            log.write_log(ws_str,"logs/coin_market_cap_log.txt")
            break
        except AttributeError as e:
            print("Error: {}\nretrying... {} / {}".format(e, i, retrys))
            time.sleep(8)


if __name__ == "__main__":
    main()
