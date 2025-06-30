from flask import Flask, request, jsonify
import requests
from flask import render_template

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["message"]
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": message}
    )
    response_data = response.json()

    if response_data:
        reply_text = response_data[0].get("text", "")
        buttons = response_data[0].get("buttons", [])
        return jsonify({"reply": reply_text, "buttons": buttons})
    else:
        return jsonify({"reply": "Sorry, I didn’t get that.", "buttons": []})

if __name__ == "__main__":
    app.run(debug=True)
