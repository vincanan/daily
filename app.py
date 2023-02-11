from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi
import jwt
import hashlib
import datetime

ca = certifi.where()
client = MongoClient('mongodb+srv://kimnoc707:vkfkd0312@cluster0.wpr6ivo.mongodb.net/?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.sparta_project


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/index')
def main():
    return render_template('index.html')


@app.route('/daily', methods=["POST"])
def daily_comment():
    date_receive = request.form['date_give']
    user_receive = request.form['user_give']
    comment_receive = request.form['comment_give']

    d_list = list(db.daily_list.find({}, {'_id': False}))
    count = len(d_list) + 1
    doc = {
        'num': count,
        'date': date_receive,
        'user': user_receive,
        'comment': comment_receive,
        'done': 0

    }
    db.daily_list.insert_one(doc)

    return jsonify({'msg': 'Daily 등록 완료'})


@app.route('/daily', methods=["GET"])
def daily_list():
    d_list = list(db.daily_list.find({}, {'_id': False}))
    return jsonify({'comments': d_list})


@app.route('/sign_up')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5004, debug=True)
