
import webscrap as ws
import log
import os

def main():
    # write coinmarketcap log
    ws_str: str = ws.get_bitcoin_coinmarketcap()
    print(ws_str)
    log.write_log(ws_str, "logs/test_log.txt")

if __name__ == "__main__":
    main()
