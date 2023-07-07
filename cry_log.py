import webscrap as ws
import logger
import os
import time
import sys


def main():
    # option handler
    if "-p" in sys.argv:
        logger.print_log()
        sys.exit()
    elif "--csv" in sys.argv:
        add_log_bitcoin(csv=True)
        add_log_xmr(csv=True)
    else:
        add_log_bitcoin()
        add_log_xmr()


def add_log_bitcoin(csv: bool=False):
    retrys = 2
    p = os.path.dirname(os.path.abspath(__file__))
    for i in range(retrys):
        try:
            (ws_str, ws_csv) = ws.get_bitcoin_coinmarketcap()

            # write coinmarketcap log
            logger.write_log(ws_str, p + "/logs/bitcoin_market_cap_log.txt")
            if csv: logger.write_csv(ws_csv, p + "/logs/bitcoin_market_cap_log.csv")
            break
        except AttributeError as e:
            print("Error: {}\nretrying... {} / {}".format(e, i, retrys))
            time.sleep(2)

    logger.write_error("error", p +"/logs/test_log.txt")


def add_log_xmr(csv: bool=False):
    retrys = 2
    p = os.path.dirname(os.path.abspath(__file__))
    for i in range(retrys):
        try:
            (ws_str, ws_csv) = ws.get_monero_coinmarketcap()

            # write coinmarketcap log
            logger.write_log(ws_str, p + "/logs/xmr_cmk.txt")
            if csv: logger.write_csv(ws_csv, p + "/logs/xmr_cmk.csv")
            break
        except AttributeError as e:
            print("Error: {}\nretrying... {} / {}".format(e, i, retrys))
            time.sleep(2)

    logger.write_error("error", p +"/logs/test_log.txt")

if __name__ == "__main__":
    main()
