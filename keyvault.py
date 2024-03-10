'''
This is the class to work with Azure key vault.
It requires to install the extension Azure Account to login your account.
'''
import os
import json
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

class keyvault:
    def __init__(self):
        load_dotenv()
        self.keyVaultName = os.environ["KEY_VAULT_NAME"]
        self.KVUri = f"https://{self.keyVaultName}.vault.azure.net"
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=self.KVUri, credential=self.credential)

    def create_secret(self):
        self.secretName = input("Input a name for your secret > ")
        self.secretValue = input("Input a value for your secret > ")
        print(f"Creating a secret in {self.keyVaultName} called '{self.secretName}' with the value '{self.secretValue}' ...")
        self.client.set_secret(self.secretName, self.secretValue)
        print(" done.")

    def load_coinbase_secret(self):
        f = open('coinbase_cloud_api_key.json')
        api_key = json.load(f)
        self.client.set_secret('name', api_key['name'])
        self.client.set_secret('privateKey', api_key['privateKey'])


    def fetch_secret(self):
        self.secretName = input("Input a name for your secret > ")
        print(f"Retrieving your secret from {self.keyVaultName}.")
        retrieved_secret = self.client.get_secret(self.secretName)
        print(f"Your secret is '{retrieved_secret.value}'.")

    def list_secret(self):
        list_secret = []
        secret_properties = self.client.list_properties_of_secrets()
        for secret_property in secret_properties:
            # the list doesn't include values or versions of the secrets
            print(secret_property.name)
            list_secret.append(secret_property.name)
        return list_secret


    def delete_secret(self):
        self.secretName = input("Input a name for your secret > ")
        print(f"Deleting your secret from {self.keyVaultName} ...")
        poller = self.client.begin_delete_secret(self.secretName)
        deleted_secret = poller.result()
        print(" done.")
    #az keyvault secret purge --vault-name crypto-trading-bot --name "name"
    
    def delete_all_secret(self):
        print("You have the following secrets in the key vault:")
        list_secret = self.list_secret()
        for secret in list_secret:
            poller = self.client.begin_delete_secret(secret)
        deleted_secret = poller.result()
        print(" done.")

if __name__ == "__main__":
    load_dotenv()
    key1 = keyvault()
    key1.load_coinbase_secret()
    #key1.list_secret()
    #key1.delete_secret()
    