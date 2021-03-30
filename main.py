from pancakeswap_scraper import Pancakeswap_scraper

# initialize, this ensures the browser is opened only once, otherwise you would run out of ram eventually (in case of
# continuous listening)
swap = Pancakeswap_scraper()

# select pair you want to listen to, possibility to pass currency amount if you don't want to check 1:many ratio
swap.select_pair(currency1="CAKE", currency2="BUSD")
print(swap.get_pair_price())

# test selecting second pair
swap.select_pair(currency1="BNB", currency2="BUSD")
print(swap.get_pair_price())