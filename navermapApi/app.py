from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongodb+srv://inseong0620:jiji9400@cluster0.vz0y2.mongodb.net/Cluster?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def main():
    return render_template("index.html")

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

@app.route('/mountain', methods=["GET"])
def get_mountain():
    # 1. 데이터베이스에서 맛집 목록을 꺼내와야 한다.
    mountain_list = list(db.mountains.find({}, {'_id': False}))
    # 2. 클라이언트에 돌려준다.
    return jsonify({'result': 'success', 'mountain_list': mountain_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)