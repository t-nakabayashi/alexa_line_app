import requests

def lambda_handler(event, context):
    if event['request']['type'] == "IntentRequest":
        intent = event['request']['intent']
        value = intent['slots']['MessageType']['value']

        url = "https://notify-api.line.me/api/notify"

        # ここにLINEのトークンを入れる
        token = "トークン"
        headers = {"Authorization" : "Bearer "+ token}

        message =  value
        payload = {"message" :  message}
        r = requests.post(url ,headers = headers ,params=payload)

        talk_message = str(value) + "とラインに通知しました"
        # リマインドメッセージがある場合はラインに通知してアプリを終える
        endSession = True
    else:
        talk_message = "なんとリマインドしますか？"
        # リマインドメッセージがない場合は何をリマインドするか確認する
        endSession = False


    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': talk_message
            },
            "shouldEndSession": endSession
        }
    }
    return response
