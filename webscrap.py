import sys
import requests
from bs4 import BeautifulSoup

# parses data from givem crypto sites
#   cur suppoorted: coin_market_cap
#   due to diferences in html structure, every website requeres his own function


# TODO make date variable for get btc price since date
# TODO get 24hrs increment for spec..
# TODO format spec_info better
def get_bitcoin_coinmarketcap() -> tuple:
    # parse content NOTE: url bugs out for unknow reason
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    print(f"Parsing from: \"{url}\"")
    # get price data

    html_resp = requests.get(url, timeout=5)
    print(f"Status: {html_resp.status_code}\t{'OK' if html_resp.ok else 'Error'}")

    html = BeautifulSoup(html_resp.text, "lxml")

    info = [stat_block.find("div", class_="statsValue").text for stat_block in html.find_all("div", class_="statsBlock")]

    label = ("price", "low", "high", "market_cap", "diluted_market_cap", "volume")
    data = [
            html.find("div", class_="priceValue").text,
            html.find("div",class_="sc-aef7b723-0 kIYhSM").find("span",class_="sc-fe06e004-5 jXIGCe").text,
            html.find("div",class_="sc-aef7b723-0 gjeJMv").find("span",class_="sc-fe06e004-5 jXIGCe").text,
            info[0], info[1], info[2],
        ]
    output_str = ""
    output_csv = ""
    for item in zip(label, data):
        output_str += "{}: {} | ".format(item[0], item[1])
        output_csv += "{};".format(item[1])
    return (output_str, output_csv)


def test(url: str) -> str:
    # test function for convenience
    if not url:
        print (f"url for: {__name__} not provided")
        sys.exit(1)



def get_bitcoin_brl():
    pass

if __name__ == "__main__":
    line = get_bitcoin_coinmarketcap()
    urls = [
            "https://www.coindesk.com/price/bitcoin/",
            " www.coinbase.com/price/bitcoin ",
            "https://markets.businessinsider.com/currencies/btc-usd?op=1",
            ]
    print(line)
