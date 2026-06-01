from binance.client import Client

API_KEY = "v8milOfcie70M818sa2FuvAZgsHwrORRUFFRRfXgtgDFNdVCLKtUa4rBXoUDdh0y"
API_SECRET = "8BoQMIQMQXjkKtZjCmQXQsWBYESx2FHkJma2qTcJ9iFMjhKxkBedGYXz6ceiKxhg" 

client = Client(API_KEY, API_SECRET )

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"