
import webscrap as ws
import log
import os

def main():
    # write coinmarketcap log
    log.write_log(ws.get_bitcoin_coinmarketcap(), os.relpath("logs/test_log.txt"))
