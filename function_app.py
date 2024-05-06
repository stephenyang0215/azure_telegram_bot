import azure.functions as func
import logging


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
BOT_URL = 'https://api.telegram.org/bot7073361003:AAE_sZJgntP95ZI6bkgocP9pe6RGWdNsbqI/'
def get_chat_id(data):
    """
    Method to extract chat id from telegram request.
    """
    chat_id = data['message']['chat']['id']
    return chat_id

def send_message(prepared_data):
    import requests

    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """
    message_url = BOT_URL + 'sendMessage'
    #func.HttpRequest(method="POST", url=message_url, body=prepared_data)
    requests.post(message_url, json=prepared_data)
@app.route(route="/")
def main(req: func.HttpRequest) -> func.HttpResponse:
    from api import get_price
    
    logging.info('Python HTTP trigger function processed a request.')
    data = req.get_json()
    #logging.info(f"Request Bytes: {data}")
    answer_data = get_price(get_chat_id(data))
    print("data: ", answer_data)
    send_message(answer_data)  # <--- function for sending answer
    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200
        )  # status 200 OK by default

@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200
        )


