from coinbase.wallet.client import Client
client = Client('organizations/0c80e088-2c8e-4894-a4aa-a5726bca5240/apiKeys/51a6419a-b323-4aff-9b82-79ec9ed420d5',
                '-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIARnanXYjVdmyyBdEvapKWkDGRTE9a8DNJUZjWMn7IdyoAoGCCqGSM49\nAwEHoUQDQgAEeqIkDGgvzcNkQ6MgsuI99EfTo5cb33aZGCg7yuiHPWWNUZmZCnk3\nTAP7Ogm7LLMW+l331IDMMnfrId0+lfaMtw==\n-----END EC PRIVATE KEY-----\n')

def get_price(chat_id):
    btc = client.get_sell_price(currency_pair='BTC-USD')
    amount = btc['amount']
    print('BTC price: ', amount)
    protfolio = round(0.2563 * float(amount), 2)
    json_data = {
        "chat_id": chat_id,
        "text": "Investing $"+str(protfolio)+
        "\nBTC price(Coinbase): "+amount+
        "\ngo check the trend:\nhttps://www.tradingview.com/chart/ZLu8MfRn/?symbol=NASDAQ%3ATSLA"
    }
    return json_data
