import requests
import datetime
import time
from bs4 import BeautifulSoup as bs
import os


def get_bitcoin_data_coinmarketcap(start_date: datetime.time, retrys: int = 10) -> str:
    # parse content
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    html_resp = requests.get(url, timeout=10)
    print(f"Parsing from: {url} \
Status: {html_resp.status_code}\t{'OK' if html_resp.ok else 'Error'}")
    # get price data
    for i in range(retrys):
        try:
            html = bs(html_resp.text, "lxml")
            price = html.find("div", class_="priceValue").text
            print(price)
            low, high = (
                    html.find("div",class_="sc-aef7b723-0 kIYhSM").find("span",class_="sc-fe06e004-5 jXIGCe").text,
                    html.find("div",class_="sc-aef7b723-0 gjeJMv").find("span",class_="sc-fe06e004-5 jXIGCe").text
                    )
            print(low, high)
            # TODO make date variable for get btc price since date
            # TODO format date in return
            return "bitcoin price: {} | 24h low: {} | 24h high: {} | date: {}".format(
                    price, low, high, datetime.datetime.now())
        except Exception as Err:
            print(f"{Err} retrying {i+1} / {retrys}")
            time.sleep(4)


def write_to_log(line: str, log: os.path) -> bool:
    pass

def get_bitcoin_brl():
    pass

#def get_btc_coinmarketcap(start_date: str, end_date:str) -> List[Dict]:
    ## build url
    #url = f"https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={start_date}&end={end_date}"
#
    ## make request and parse tree
    #response = requests.get(url, timeout=5)
    #tree = lxml.html.fromstring(response.text)
    ## extract data
    #table = tree.find_class("cmc-table")[0]
    #xpath_0, xpath_1 = 'div[3]/div/table/thead/tr', 'div[3]/div/table/tbody/tr/td[%d]/div'
    ## process data
    #cols = [_.text_content() for _ in table.xpath(xpath_0 + '/th')]
    #dates = (_.text_content() for _ in table.xpath(xpath_1 % 1))
    #m = map(lambda d: (float(_.text_content().replace(',', '')) for _ in table.xpath(xpath_1 % d)),
            #range(2, 8))
    #return [{k: v for k, v in zip(cols, _)} for _ in zip(dates, *m)]

if __name__ == "__main__":
    print("Hello World")
    line = get_bitcoin_data_coinmarketcap(datetime.datetime.now())
    print(line)
