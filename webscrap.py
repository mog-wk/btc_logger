import sys
import requests
from bs4 import BeautifulSoup

# parses data from givem crypto sites
#   cur suppoorted: coin_market_cap
#   due to diferences in html structure, every website requeres his own function


# TODO make date variable for get btc price since date
# TODO get 24hrs increment for spec..
# TODO make high increment of data scrapping

def get_bitcoin_coinmarketcap() -> tuple:
    '''scrap bitcoin price for coin marketcap
    returns parsed data: (price; low, high, market_cap, diluted_market_cap, volume)'''

    # parse content NOTE: url bugs out for unknow reason
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    print(f"Parsing from: \"{url}\"")
    # get price data

    html_resp = requests.get(url, timeout=5)
    print(f"Status: {html_resp.status_code}\t{'OK' if html_resp.ok else 'Error'}")

    html = BeautifulSoup(html_resp.text, "lxml")

    info = [stat_block.find("div", class_="statsValue").text[1:] for stat_block in html.find_all("div", class_="statsBlock")]

    #label = ("price", "low", "high", "market_cap", "diluted_market_cap", "volume")
    label = ("price", "low", "high", "market_cap", "volume")
    data = [
            html.find("div", class_="priceValue").text[1:],
            html.find("div",class_="sc-aef7b723-0 kIYhSM").find("span",class_="sc-fe06e004-5 jXIGCe").text[1:],
            html.find("div",class_="sc-aef7b723-0 gjeJMv").find("span",class_="sc-fe06e004-5 jXIGCe").text[1:],
            info[0], info[2],
        ]
    output_str = ""
    output_csv = ""
    for item in zip(label, data):
        output_str += "{}: {} | ".format(item[0], item[1])
        output_csv += "{};".format(item[1])
    return (output_str, output_csv)


def get_monero_coinmarketcap(DEBUG=False):
    ''' get monero(XMR) data from coinmarketcap, all prices in USD'''
    url = "https://coinmarketcap.com/currencies/monero/"
    if DEBUG: print(f"Parsing from: \"{url}\"")
    html_resp = requests.get(url, timeout=5)
    print(f"Status: {html_resp.status_code}\t{'OK' if html_resp.ok else 'Error'}")
    html = BeautifulSoup(html_resp.text, "lxml")

    label = ("price", "low", "high", "market_cap", "volume")
    try:
        price = html.find("span", class_="dxubiK")
        low, high = html.find("div", class_="sc-16891c57-0 gPFIPZ flexBetween").find_all("span")
        market_cap, volume, density, circulating_supply, total_supply, max_supply, fully_diluted_market_cap = (i for i in html.find_all("dd", class_="sc-16891c57-0 fRWxhs base-text"))
        data = [
                price.text, low.text, high.text, market_cap.text.split("%")[1], volume.text.split("%")[1], '%' + density.text[:-1]
                ]

        output_str = ""
        output_csv = ""
        for item in zip(label, data):
            output_str += "{}: {} | ".format(item[0], item[1])
            output_csv += "{};".format(item[1][1:])
        return (output_str, output_csv)

    except AttributeError as e:
        print(f"unable to recover XMR, this usually means the website is updating,\nthe scrapper should work fine in a couple minutes")
        if DEBUG: print(f"Error: {e}")
        raise e
    except:
        print(f"unable to scrap XMR unknow error prease report...")
    return (None, None)


    
def test(url: str) -> str:
    # test function for convenience
    if not url:
        print (f"url for: {__name__} not provided")
        sys.exit(1)



def get_bitcoin_brl():
    pass

if __name__ == "__main__":
    line = get_monero_coinmarketcap(DEBUG=True)
    urls = [
            "https://www.coindesk.com/price/bitcoin/",
            " www.coinbase.com/price/bitcoin ",
            "https://markets.businessinsider.com/currencies/btc-usd?op=1",
            ]
    print(line)

