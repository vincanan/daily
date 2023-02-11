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

client = MongoClient('mongodb+srv://kimnoc707:vkfkd0312@cluster0.wpr6ivo.mongodb.net/?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.sparta_project

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


@app.route("/daily/done", methods=["POST"])
def daily_done():
    num_receive = request.form['num_give']
    db.daily_list.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    # 데이터가 넘어올때 문자타입으로 넘어오므로 int타입으로 형변환 시켜줘야함

    return jsonify({'msg': 'Daily 완료!'})


@app.route("/daily/cancel", methods=["POST"])
def daily_cancel():
    num_receive = request.form['num_give']
    db.daily_list.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
    # 데이터가 넘어올때 문자타입으로 넘어오므로 int타입으로 형변환 시켜줘야함

    return jsonify({'msg': 'Daily 취소!'})


@app.route('/todo', methods=["POST"])
def todo_comment():
    date_receive = request.form['date_give']
    user_receive = request.form['user_give']
    comment_receive = request.form['comment_give']

    t_list = list(db.todo_list.find({}, {'_id': False}))
    count = len(t_list) + 1
    doc = {
        'num': count,
        'date': date_receive,
        'user': user_receive,
        'comment': comment_receive,
        'done': 0

    }
    db.todo_list.insert_one(doc)

    return jsonify({'msg': 'To-do 등록 완료'})


@app.route('/todo', methods=["GET"])
def todo_list():
    t_list = list(db.todo_list.find({}, {'_id': False}))
    print(t_list)
    return jsonify({'comments': t_list})


@app.route("/todo/done", methods=["POST"])
def todo_done():
    num_receive = request.form['num_give']
    db.todo_list.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    # 데이터가 넘어올때 문자타입으로 넘어오므로 int타입으로 형변환 시켜줘야함

    return jsonify({'msg': 'To-do 완료!'})


@app.route("/todo/cancel", methods=["POST"])
def todo_cancel():
    num_receive = request.form['num_give']
    db.todo_list.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
    # 데이터가 넘어올때 문자타입으로 넘어오므로 int타입으로 형변환 시켜줘야함

    return jsonify({'msg': 'To-do 취소!'})


@app.route('/study', methods=["POST"])
def study_comment():
    date_receive = request.form['date_give']
    user_receive = request.form['user_give']
    comment_receive = request.form['comment_give']

    s_list = list(db.study_list.find({}, {'_id': False}))
    count = len(s_list) + 1
    doc = {
        'num': count,
        'date': date_receive,
        'user': user_receive,
        'comment': comment_receive,
        'done': 0

    }
    db.study_list.insert_one(doc)

    return jsonify({'msg': 'Study 등록 완료'})


@app.route('/study', methods=["GET"])
def study_list():
    s_list = list(db.study_list.find({}, {'_id': False}))
    return jsonify({'comments': s_list})


@app.route("/study/done", methods=["POST"])
def study_done():
    num_receive = request.form['num_give']
    db.study_list.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    # 데이터가 넘어올때 문자타입으로 넘어오므로 int타입으로 형변환 시켜줘야함

    return jsonify({'msg': 'Study 완료!'})


@app.route("/study/cancel", methods=["POST"])
def study_cancel():
    num_receive = request.form['num_give']
    db.study_list.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
    # 데이터가 넘어올때 문자타입으로 넘어오므로 int타입으로 형변환 시켜줘야함

    return jsonify({'msg': 'Study 취소!'})


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

@app.route('/api/nick', methods=['GET'])
def api_valid():
        token_receive = request.cookies.get('mytoken')

        try:
            # token을 시크릿키로 디코딩합니다.
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            print(payload)

            # payload 안에 id가 들어있습니다.
            # 여기에선 그 예로 닉네임을 보내
            userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
            return jsonify({'result': 'success', 'nickname': userinfo['nick']})
        except jwt.ExpiredSignatureError:
            # 위를 실행했는데 만료시간이 지났으면 에러
            return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
        except jwt.exceptions.DecodeError:
            return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
