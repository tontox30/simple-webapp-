# app.py
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "welcome1"

@app.route('/how are you')
def hello():
    return 'i am good, how about you?'

if __name__ == "__main__":
    app.run()

