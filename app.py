import streamlit as st
import requests

apikey = "DZZixcVPZqTWl5MQu1dVAwty2N8qnjyH"

#チャットのやり取りを記録するリスト
chat_logs = []

#アプリのタイトル
st.title("Chatbot with streamlit")

#headerのテキスト表示とテキスト入力ウインドウ
st.subheader("メッセージを入力してから送信をタップしてください")
message = st.text_input("メッセージ")

#チャットボットAPIを呼び出す
def send_pya3rt(endpoint,apikey,text,callback):
    params = {
        'apikey':apikey,
        'query':text,
    }
    if callback is not None:
        params['callback'] = callback
        
    response = requests.post(endpoint,params)
    
    return response.json()

#ボタンが選択されたときに呼び出される関数
def generate_response():
    ans_json = send_pya3rt('https://api.a3rt.recruit.co.jp/talk/v1/smalltalk',apikey,message,None)
    ans = ans_json['results'][0]['reply']
    chat_logs.append('you:'+message)
    chat_logs.append('bot:'+ans)
    for chat_log in chat_log:
        st.write(chat_log)
        
if st.button("送信"):
    generate_response()