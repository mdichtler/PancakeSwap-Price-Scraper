# PancakeSwap Price Scraper

#INSTALLATION INSTRUCTIONS:

Install chrome & get chrome driver of appropriate version: https://chromedriver.chromium.org/downloads 

After downloading Chrome Driver, place it inside the project directory, to folder ./drivers/chromedriver.exe

Since the scraper has support for multiple exchanges (running pancakeswap.finance frontend), arguments can be used to specify pair that should be tracked, different exchange url as well as alias that will be showed in the db instead of the url:

``--c1`` -> currency1, type: str, default: BNB

``--c2`` -> currency2, type: str, default: BUSD

``--ex`` -> target_exchange, type: str, default: https://exchange.pancakeswap.finance/#/swap

``--exalias`` -> exchange_alias, type: str, default: PANCAKESWAP


#Packages used:

``selenium`` 

