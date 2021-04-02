from pancakeswap_scraper import Pancakeswap_scraper
from firebase_interface import  Firebase_Interface
# initialize, this ensures the browser is opened only once, otherwise you would run out of ram eventually (in case of
# continuous listening)
swap = Pancakeswap_scraper()
# instead of . / etc we are using _
fb = Firebase_Interface(scraped_site="pancakeswap_finance")
# select pair you want to listen to, possibility to pass currency amount if you don't want to check 1:many ratio
currency1 = input("Enter First Currency: ")
currency2 = input("Enter Second Currency: ")

swap.select_pair(currency1=currency1, currency2=currency2)

old_value = None
while True:
    # get price
    data, format = swap.get_pair_price()
    if old_value == data["value"]:
        pass
    else:
        # only do update on price change
        old_value = data["value"]
        fb.save_data(pair=format["pair"], date=format["date"], time=format["time"], seconds=format["seconds"], data=data)
        print("Saving data: ", data, format)




