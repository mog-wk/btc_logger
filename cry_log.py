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
    else:
        add_log()


def add_log():
    retrys = 1
    p = os.path.dirname(os.path.abspath(__file__))
    print(p)
    for i in range(retrys):
        try:
            ws_str: str = ws.get_bitcoin_coinmarketcap()

            # write coinmarketcap log
            #logger.write_log(ws_str, p + "/logs/test_log.txt")
            logger.write_log(ws_str, p + "/logs/coin_market_cap_log.txt")
            break
        except AttributeError as e:
            print("Error: {}\nretrying... {} / {}".format(e, i, retrys))
            time.sleep(2)

    logger.write_error("cron_test_error", p + "/logs/test_log.txt")

if __name__ == "__main__":
    main()
