import requests

response = requests.get('https://api.kraken.com/0/public/Time')

print(response.json())
