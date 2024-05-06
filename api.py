from coinbase.wallet.client import Client
from keyvault import keyvault

def get_price(chat_id):
    key1 = keyvault()
    client = (key1.fetch_secret('name').value, 
                    key1.fetch_secret('privateKey').value)
    btc = client.get_sell_price(currency_pair='BTC-USD')
    price = btc['amount']
    print('BTC price: ', price)
    json_data = {
        "chat_id": chat_id,
        "text": "BTC price(Coinbase): "+price
    }
    return json_data
if __name__ == "__main__":
    key1 = keyvault()
    client = Client(key1.fetch_secret('name').value, 
                    key1.fetch_secret('privateKey').value)
    btc = client.get_sell_price(currency_pair='BTC-USD')
    amount = btc['amount']
    print('BTC price: ', amount)