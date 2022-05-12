from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from connection import s3_connection
from config import BUCKET_NAME
import boto3
from botocore.client import Config







app = Flask(__name__)

client = MongoClient('mongodb+srv://inseong0620:jiji9400@cluster0.vz0y2.mongodb.net/Cluster?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def main():
    return render_template("login.html")


@app.route('/check')
def Check():
    return render_template("check.html")

@app.route('/HanLa')
def HanLa():
    return render_template("HanLa.html")

@app.route('/Seorak')
def Seorak():
    return render_template("Seorak.html")

@app.route('/Gwanag')
def Gwanag():
    return render_template("Gwanag.html")

@app.route('/Dubong')
def Dubong():
    return render_template("Dubong.html")

@app.route('/GiRi')
def GiRi():
    return render_template("GiRi.html")


@app.route('/mypage')
def mypage():
    return render_template("mypage.html")





@app.route('/mountain', methods=["GET"])
def get_mountain():
    # 1. 데이터베이스에서 산 목록을 꺼내와야 한다.
    mountain_list = list(db.mountains.find({}, {'_id': False}))
    # 2. 클라이언트에 돌려준다.
    return jsonify({'result': 'success', 'mountain_list': mountain_list})


SECRET_KEY = 'SPARTA'


@app.route('/first')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})

        return render_template('first.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')\
            # .decode('utf-8') # git bash 오류 해결 코드

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": username_receive,                           # 프로필 이름 기본값은 아이디
        # "useremail": "",                                          # 유저 이메일
        # "profile_pic_real": "profile_pics/profile_placeholder.png", # 프로필 사진 기본 이미지
        # "profile_info": ""                                          # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/HanLa', methods=['POST'])
def hanLa_post():
    s3 = s3_connection()
    data = request.form['image-0']


    s3 = boto3.resource(
        's3',
        aws_access_key_id='AKIAWBXANJBJK75PIVV3',
        aws_secret_access_key='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',
        config=Config(signature_version='s3v4')
    )
    s3.Bucket('mountaingo').put_object(

        Key=f'images/{data}', Body=data, ContentType='image/jpeg')

    return jsonify({'msg': 'success!!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)