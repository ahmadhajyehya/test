import requests

from_coin = 'USD'
to_coin = 'ILS'
amount = '1'
url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_coin}&from={from_coin}&amount={amount}"

payload = {}
headers = {
  "apikey": "XXXXXXXXXXXX"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
print(result)
