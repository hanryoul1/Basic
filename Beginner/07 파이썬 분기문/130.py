import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# {"status":"0000",\
#     "data":{"opening_price":"23003000","closing_price":"23024000",\
#         "min_price":"22868000","max_price":"23089000","units_traded":"954.10791369","acc_trade_value":"21922045824.9855","prev_closing_price":"23001000","units_traded_24H":"1243.96329846","acc_trade_value_24H":"28598592950.9557","fluctate_24H":"36000","fluctate_rate_24H":"0.16","date":"1668852303631"}}
print(btc)
op = int(btc["opening_price"])
cp = int(btc["closing_price"])
minp = int(btc["min_price"])
maxp = int(btc["max_price"])
change = maxp - minp

if op + change > maxp:
    print("상승장")

else:
    print("하락장")