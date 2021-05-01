import argparse

from scraper import Scraper
from sqlite import sqliteDB

parser = argparse.ArgumentParser(description="Parser")
parser.add_argument("--c1", type=str, default="BNB")
parser.add_argument("--c2", type=str, default="BUSD")
parser.add_argument(
    "--ex", type=str, default="https://exchange.pancakeswap.finance/#/swap"
)
parser.add_argument("--exalias", type=str, default="PANCAKESWAP")
parser.add_argument("--reverse", type=bool, default=False)

# user can specify chrome binary using --path parameter if not in default location
parser.add_argument("--path", type=str, default="C:\Program Files\Google\Chrome\Application\chrome.exe")

args = parser.parse_args()

# parse parameters from run command
currency1 = args.c1
currency2 = args.c2
target_exchange = args.ex
exchange_alias = args.exalias
reverse = args.reverse
bin_path = args.path

db = sqliteDB()

# check if table already exists, otherwise create it
db._table_exists()

# url defaults to pancakeswap.finance if not provided
if target_exchange == "":
    scraper = Scraper(url="https://exchange.pancakeswap.finance/#/swap", bin_path=bin_path)
else:
    scraper = Scraper(url=target_exchange, bin_path=bin_path)

scraper.select_pair(currency1=currency1, currency2=currency2, reverse=reverse)

# update in infinite loop
old_value = None
while True:
    # get price
    data = scraper.get_pair_price()
    if old_value == data["value"]:
        pass
    else:
        # only do update on price change
        old_value = data["value"]
        # check if exchange alias is empty, if yes use default
        if exchange_alias == "":
            db.insert_record(
                datetime=data["time"],
                exchange="https://exchange.pancakeswap.finance/#/swap",
                pair=data["pair"],
                value=data["value"],
            )
        else:
            db.insert_record(
                datetime=data["time"],
                exchange=exchange_alias,
                pair=data["pair"],
                value=data["value"],
            )
        print("Saving data: ", data, format)
