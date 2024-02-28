from coinbase.wallet.client import Client
client = Client('organizations/0c80e088-2c8e-4894-a4aa-a5726bca5240/apiKeys/51a6419a-b323-4aff-9b82-79ec9ed420d5',
                '-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIARnanXYjVdmyyBdEvapKWkDGRTE9a8DNJUZjWMn7IdyoAoGCCqGSM49\nAwEHoUQDQgAEeqIkDGgvzcNkQ6MgsuI99EfTo5cb33aZGCg7yuiHPWWNUZmZCnk3\nTAP7Ogm7LLMW+l331IDMMnfrId0+lfaMtw==\n-----END EC PRIVATE KEY-----\n')

btc = client.get_sell_price(currency_pair = 'BTC-USD')
amount = btc['amount']
print('BTC price: ', amount)
protfolio = round(0.2563*float(amount),2)
print('Total amount for the client: ', protfolio)