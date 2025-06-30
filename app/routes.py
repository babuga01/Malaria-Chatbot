from flask import Blueprint, render_template, request, jsonify
import requests

main = Blueprint('main', __name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})
    
    if response.status_code == 200:
        messages = response.json()
        bot_reply = ' '.join([msg.get('text', '') for msg in messages])
        return jsonify({'reply': bot_reply})
    else:
        return jsonify({'reply': 'Error communicating with chatbot backend.'})
