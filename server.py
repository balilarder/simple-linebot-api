from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


import json

from datetime import datetime
from model_setup import UserMessage

from model_setup import myclient, db_name, collection_name

app = Flask(__name__)


# LineBot configuration: Channel Access Token & channel secret
line_bot_api = LineBotApi('mVlDuD7Nl3YsM6wlT4qfncK3v7LgXwBpVu+4gFt6vnRQPOVlY4E3rWyE38hrrP0Pp/MlgpW0DwmAP2gWERvULbjx7QbJlG/2Tyuyd9JY1o9OnSMKEwuSwnMijMfOUqv+to59cmc/uV5/T6ABXwV0GwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f91311c541fde8ca90ee5ce0eb40e8d')

@app.route("/test", methods=['GET'])
def test():
    return "Hello World"


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']  # the signature confirm that the message is from line.
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'Succeed'

@handler.add(MessageEvent, message=TextMessage)
def save_message(event):
    
    # fetch the useid and the message text:
    user_id = event.source.user_id
    user_message = event.message.text
    timestamp = datetime.fromtimestamp(event.timestamp / 1000)
    
    print(user_id, user_message, str(timestamp))
    print(type(user_id), type(user_message), type(timestamp))
    insert_into_mongo(user_id, user_message, str(timestamp))

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f" {user_message}, Message has been saved"))




def insert_into_mongo(user_id, user_message, timestamp):
    print(f"Ready to write a message to {collection_name}")
    message = UserMessage(user_id=user_id, user_message=user_message, timestamp=timestamp)
    mydb = myclient[db_name]
    mycollection = mydb[collection_name]
    mycollection.insert_one(message.__dict__)   # Add a document into mongodb


@app.route("/broadcast", methods=['POST'])
def broadcast():
    '''
    request body: json:
    {"message":"MESSAGE_TO_BROADCAST"}
    '''
    # parse the request body
    parameter = request.get_json()
    try:
        broadcast_message = parameter['message']
    except:
        app.logger.info('Parse request body failed. json format is {"message": "MESSAGE_TO_BROADCAST"}')    

    
    try:
        response = line_bot_api.broadcast(TextSendMessage(text=broadcast_message))
        print(str(response), response.__dict__)
        return 'Succeed'
    except:
        app.logger.info("Broadcast failed.")



if __name__ == "__main__":
    app.run()