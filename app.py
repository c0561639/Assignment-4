from dotenv import load_dotenv; load_dotenv()
from flask import Flask, Response
import os

app = Flask(__name__)

@app.get("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello from Flask (set APP_MESSAGE)!")
    return Response(message, mimetype="text/plain")

@app.get("/health")
def health():
    status = os.getenv("APP_HEALTH", "OK")
    return Response(status, mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
