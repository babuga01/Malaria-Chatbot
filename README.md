# 🦟 Malaria Chatbot Assistant

The **Malaria Chatbot Assistant** is an AI-powered conversational system developed to raise awareness, provide health information, and guide users about 
**malaria symptoms, prevention, treatment, and transmission**. It is built using **Rasa Open Source**, **Flask**, and a responsive web interface using **HTML**, **CSS**, and **JavaScript**.


## 🚀 Features

- ✅ Malaria symptom checker
- ✅ Educational responses on causes, prevention, treatment, and transmission
- ✅ Intelligent intent recognition using NLP
- ✅ Interactive chatbot with quick replies and dynamic buttons
- ✅ Timestamped conversation flow
- ✅ Runs locally on your machine


## 🧰 Technologies Used

| Component   | Description                                |
|-------------|--------------------------------------------|
| 🧠 Rasa      | Natural Language Processing (NLU) and Dialogue Management |
| 🌐 Flask     | Backend server for chatbot integration     |
| 💬 HTML/CSS | Frontend chatbot interface                 |
| 🧩 JavaScript | Chat message handling and button interaction |
| 🐍 Python    | Core programming language used             |


## 📂 Project Structure

```

Malaria-Chatbot/
│
├── chatbot/
│   ├── data/
│   │   ├── nlu.yml
│   │   ├── rules.yml
│   │   └── stories.yml
│   ├── domain.yml
│   ├── config.yml
│   ├── actions.py
│   └── endpoints.yml
│
├── app/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   └── routes.py
│
├── run.py
├── requirements.txt
└── README.md

````


## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Malaria-Chatbot.git
cd Malaria-Chatbot
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train Rasa Model

```bash
cd chatbot
rasa train
```


## ▶️ Running the Project Locally

> Run these in **separate terminals**, all under your project folder:

### 1️⃣ Start the Rasa Server

```bash
cd chatbot
rasa run
```

### 2️⃣ Start the Rasa Action Server

```bash
cd chatbot
rasa run actions
```

### 3️⃣ Start the Flask App

```bash
cd ..
python run.py
```

Then open your browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**


## 💡 Future Enhancements

* Add multilingual support
* Store conversation logs in a database
* Integrate with WhatsApp or Messenger
* Expand to other diseases beyond malaria


## 👤 Author

**Alamin Bashir Babuga**
Final Year Project – Malaria Chatbot Assistant

Built with ❤️ using Rasa & Flask

---

## License

This project is licensed for educational purposes.
