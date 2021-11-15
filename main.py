import requests


url = 'https://www.nseindia.com/api/corporates-pit?index=equities&from_date="Day"-"Month"-"Year"&to_date="Day"-"Month"-"Year"'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'DNT': '1',
    'Accept': 'application/json, text/javascript, */*, q=0.01',
    'Accept-Language':'es-AR,es;q=0.9,en-GB;q=0.8,en;q=0.7,es-419;q=0.6',
    'Accept-Encoding': 'gzip, deflate, br',
    'cookie': 'cookies'}

data = requests.get(url, headers=headers,timeout=25).json()

sell_list = []
res = []

            
for d in data['data']:
    if not ((d["personCategory"] == "Promoters" or d["personCategory"] == "Promoter Group") and d['acqMode'] == 'Market Purchase') and d['symbol'] not in sell_list:
        sell_list.append(d['symbol'])

for d in data['data']:
    # Checking if the item has order = buy and check if it already have order = sell
    if  ((d["personCategory"] == "Promoters" or d["personCategory"] == "Promoter Group") and d['acqMode'] == 'Market Purchase') and d['symbol'] not in sell_list and d['symbol'] not in res:
        res.append(d['symbol'])




out_set = []
great = []
good_fin = []
scrap = []
good_promoters = []
no_sast = []
yes_sast = []
def corpInfo(symbol):
    url2 = f'https://www.nseindia.com/api/quote-equity?symbol={symbol}&section=corp_info'
    info = requests.get(url2, headers=headeres, timeout=35).json()

    if 'corporate' in info:
      #PLEDGED DETAILS
        if len(info['corporate']['pledgedetails']) > 0:
            for d in info['corporate']['pledgedetails']:
                try:
                    if float(d['per1']) < 25.0 or float(d['per2']) != 0.00 or float(d['per3']) != 0.00:
                        break
                    else:good_promoters.append(symbol)
                except:
                    pass



    else:
        scrap.append(symbol)

for i in res:
    corpInfo(i)

print(good_promoters)


