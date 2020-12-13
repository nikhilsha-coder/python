import requests as req
import time
import cbpro as cbp
test_var = 10
startMoney = 100
lotSplit = 0.05
ILA = []
CVL = [] 
priceList = []


public_client = cbp.PublicClient()
buyPrice = float(public_client.get_product_ticker('BTC-USD')['price'])
currentPrice = float(public_client.get_product_ticker('BTC-USD')['price'])

#while True:
for i in range(1):
    time.sleep(1)
    currentPrice = float(public_client.get_product_ticker('BTC-USD')['price'])
    print(currentPrice)
    priceList.append(currentPrice)
    if currentPrice >= (buyPrice * 1.02) or currentPrice <= (buyPrice * 0.98):
        print('SELL')
        break
