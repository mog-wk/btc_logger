import requests
from bs4 import BeautifulSoup


# TODO make date variable for get btc price since date
# TODO format date in return
# TODO get 24hrs increment for spec..
# TODO format spec_info better
def get_bitcoin_coinmarketcap() -> str:
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
    for item in zip(label, data):
        output_str += "{}: {} | ".format(item[0], item[1])
    return output_str


def test() -> str:
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    html_resp = requests.get(url, timeout=5)
    print(f"Status: {html_resp.status_code}\t{'OK' if html_resp.ok else 'Error'}")

    html = BeautifulSoup(html_resp.text, "lxml")

    price = html.find("div", class_="sc-8755d3ba-0 cQuGMr coin-stats-header")
    print(price)
    low, high = (
            html.find("div",class_="sc-8755d3ba-0 iausdo"),
            html.find("div",class_="sc-8755d3ba-0 iausdo tlr"),
            )
    print(low, high)
    return "bitcoin price: {} | 24h low: {} | 24h high: {} | date: {}".format(
            price, low, high)


def get_bitcoin_brl():
    pass

if __name__ == "__main__":
    line = get_bitcoin_coinmarketcap()
    print(line)
