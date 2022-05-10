from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.b7vsn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta




@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    # print(sample_receive)


    doc = {
        'name' : name_receive,
        'comment' : comment_receive
    }

    db.homework.insert_one(doc)

    return jsonify({'msg':'응원 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():

    comment_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)
