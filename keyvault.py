'''
This is the class to work with Azure key vault.
It requires to install the extension Azure Account to login your account.
'''
import os
import json
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential
from dotenv import load_dotenv

class keyvault:
    def __init__(self):
        #Set up your environment variables
        load_dotenv()
        self.keyVaultName = os.environ["KEY_VAULT_NAME"]
        #Your Vault URI
        self.KVUri = f"https://{self.keyVaultName}.vault.azure.net"
        #Set up your managed identity credential
        self.credential = ManagedIdentityCredential(
            AZURE_CLIENT_ID="b7f9cc31-ae4f-4181-9c56-59e7d5aad416"
            )
        #Set up your client for Key Vault service
        self.client = SecretClient(vault_url=self.KVUri, credential=self.credential)
        
    #The function to create your secret on Key Vault
    def create_secret(self):
        self.secretName = input("Input a name for your secret > ")
        self.secretValue = input("Input a value for your secret > ")
        print(f"Creating a secret in {self.keyVaultName} called '{self.secretName}' with the value '{self.secretValue}' ...")
        self.client.set_secret(self.secretName, self.secretValue)
        print(" done.")

    #The function to load the credentials to Key Vault
    def load_coinbase_secret(self):
        f = open('coinbase_cloud_api_key.json')
        api_key = json.load(f)
        self.client.set_secret('name', api_key['name'])
        self.client.set_secret('privateKey', api_key['privateKey'])
        print(" done.")

    #The function to fetch the secrets stored in Key Vault
    def fetch_secret(self, secretName):
        retrieved_secret = self.client.get_secret(secretName)
        return retrieved_secret

    #The function to list the properties for the secrets stored in Key Vault
    def list_secret(self):
        list_secret = []
        secret_properties = self.client.list_properties_of_secrets()
        for secret_property in secret_properties:
            # the list doesn't include values or versions of the secrets
            print(secret_property.name)
            list_secret.append(secret_property.name)
        return list_secret

    #The function to delete the secrets stored in Key Vault
    def delete_secret(self):
        self.secretName = input("Input a name for your secret > ")
        print(f"Deleting your secret from {self.keyVaultName} ...")
        poller = self.client.begin_delete_secret(self.secretName)
        deleted_secret = poller.result()
        print(" done.")
    
    #The function to delete all of the secrets stored in Key Vault
    def delete_all_secret(self):
        print("You have the following secrets in the key vault:")
        list_secret = self.list_secret()
        for secret in list_secret:
            poller = self.client.begin_delete_secret(secret)
        deleted_secret = poller.result()
        print(" done.")
    