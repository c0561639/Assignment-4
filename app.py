from dotenv import load_dotenv; load_dotenv()
from flask import Flask, Response, render_template
import os

app = Flask(__name__)

def get_message():
    return os.getenv("APP_MESSAGE", "Howdy!")

def get_health():
    return os.getenv("APP_HEALTH", "OK")

@app.get("/")
def home():
    return render_template("index.html", message=get_message(), health=get_health())

@app.get("/message")
def message():
    return get_message()

@app.get("/health")
def health():
    return get_health()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
