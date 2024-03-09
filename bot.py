import requests
from keyvault import keyvault
from api import get_price
from bottle import (
    run, post, response, request as bottle_request
)
BOT_URL = 'https://api.telegram.org/bot7073361003:AAE_sZJgntP95ZI6bkgocP9pe6RGWdNsbqI/'
def get_chat_id(data):
    """
    Method to extract chat id from telegram request.
    """
    chat_id = data['message']['chat']['id']
    return chat_id
def get_message(data):
    """
    Method to extract message id from telegram request.
    """
    message_text = data['message']['text']
    return message_text
def send_message(prepared_data):
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)
@post('/')
def main():
    data = bottle_request.json
    answer_data = get_price(get_chat_id(data))
    print(answer_data)
    send_message(answer_data)  # <--- function for sending answer
    return response  # status 200 OK by default
if __name__ == '__main__':
    #run(host='localhost', port=8080, debug=True)
    azure = keyvault()
    azure.list_secret()