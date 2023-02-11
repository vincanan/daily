from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi
# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt
# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib
# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime


ca = certifi.where()
<<<<<<< HEAD
client = MongoClient('mongodb+srv://kimnoc707:vkfkd0312@cluster0.wpr6ivo.mongodb.net/?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.sparta_project

=======
client = MongoClient('mongodb+srv://test:sparta@cluster0.qli9s79.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta
>>>>>>> hojii

SECRET_KEY = 'hojii'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/index')
def main():
    return render_template('index.html')


<<<<<<< HEAD
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


=======
>>>>>>> hojii
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
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.login.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        # payload 는 담고싶은 정보(필수),secret key 암호화키
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
        # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5004, debug=True)
