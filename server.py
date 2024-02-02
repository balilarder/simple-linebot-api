from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)


# LineBot configuration: Channel Access Token & channel secret
line_bot_api = LineBotApi('mVlDuD7Nl3YsM6wlT4qfncK3v7LgXwBpVu+4gFt6vnRQPOVlY4E3rWyE38hrrP0Pp/MlgpW0DwmAP2gWERvULbjx7QbJlG/2Tyuyd9JY1o9OnSMKEwuSwnMijMfOUqv+to59cmc/uV5/T6ABXwV0GwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f91311c541fde8ca90ee5ce0eb40e8d')


@app.route("/test", methods=['GET'])
def test():
    return "Hello World"



if __name__ == "__main__":
    app.run()