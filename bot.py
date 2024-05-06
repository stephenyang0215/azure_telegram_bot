import requests
from keyvault import keyvault
from api import get_price
import os
from bottle import (
    run, post, response, request as bottle_request
)

BOT_URL = os.environ["BOT_URL"]

#Receive chat id from the request.
def get_chat_id(data):
    chat_id = data['message']['chat']['id']
    return chat_id

#Receive message id from the request.
def get_message(data):
    message_text = data['message']['text']
    return message_text

#Prepared data should be json which includes at least `chat_id` and `text`
def send_message(prepared_data):
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)

#Execute the process
@post('/')
def main():
    data = bottle_request.json
    answer_data = get_price(get_chat_id(data))
    print(answer_data)
    send_message(answer_data)  # <--- function for sending answer
    return response  # status 200 OK by default
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)