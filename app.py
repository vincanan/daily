from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
import jwt
import hashlib
import datetime

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.qli9s79.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
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
def sign_up():
    return render_template('sign_up.html')


@app.route('/api/signup', methods=['POST'])
def api_signup():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_pw_receive = request.form['pw_pw_give']
    nickname_receive = request.form['nickname_give']

    check = db.login.find_one({'id': id_receive})

    if check is not None:
        return jsonify({'msg': '이미 존재하는 아이디입니다 !'})
    elif pw_receive != pw_pw_receive:
        return jsonify({'msg': '패스워드가 일치하지 않습니다 !'})
    else:
        pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
        db.login.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

        return jsonify({'result': 'success', 'msg': '회원가입 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5004, debug=True)
