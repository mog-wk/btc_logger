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
        add_log(csv=True)
    else:
        add_log()


def add_log(csv: bool=False):
    retrys = 2
    p = os.path.dirname(os.path.abspath(__file__))
    for i in range(retrys):
        try:
            (ws_str, ws_csv) = ws.get_bitcoin_coinmarketcap()

            # write coinmarketcap log
            logger.write_log(ws_str, p + "/logs/coin_market_cap_log.txt")
            if csv:
                logger.write_csv(ws_csv, p + "/logs/coin_market_cap_log.csv")
            break
        except AttributeError as e:
            print("Error: {}\nretrying... {} / {}".format(e, i, retrys))
            time.sleep(2)

    logger.write_error("error", p +"/logs/test_log.txt")


if __name__ == "__main__":
    main()
