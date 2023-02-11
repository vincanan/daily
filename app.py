from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
import jwt
import hashlib
import datetime

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.0x2me9v.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/sign_up')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5004, debug=True)
