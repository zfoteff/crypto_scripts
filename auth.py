from dotenv import load_dotenv
from coinbase.wallet.client import Client
import os
load_dotenv()

API_KEY = os.environ.get('API_KEY').encode()
API_SECRET = os.environ.get('API_SECRET').encode()
API_URL = 'https://api.coinbase.com/v2'

client = Client(API_KEY, API_SECRET)
print(f"Sell: {client.get_sell_price(currency_pair='BTC-USD').amount}")
print(f"Spot: {client.get_spot_price(currency_pair='BTC-USD').amount}")
print(f"Accounts: {client.get_current_user()}")