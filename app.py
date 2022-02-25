from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/test/test.html')
def test():
   return render_template('/test/test.html')


@app.route('/test/test2.html')
def test2():
   return render_template('/test/test2.html')


@app.route('/test/test3.html')
def test3():
   return render_template('/test/test3.html')


@app.route('/test/test4.html')
def test4():
   return render_template('/test/test4.html')


@app.route('/test/result.html')
def result():
   return render_template('/test/result.html')


@app.route('/pref', methods=['GET'])
def test_food():
   target_food = db.foods.find_one({'누적': 4})
   return jsonify({'result':'success', 'foodName': target_food['name'], 'foodImgUrl': target_food['img_url']})


@app.route('/pref2', methods=['POST'])
def like_spicy():
   spicy_receive = request.form['spicy_give']

   target_food = db.foods.find_one({'맵기': spicy_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'맵기': spicy_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '질문 2로 가주세요!'})


@app.route('/pref3', methods=['POST'])
def unlike_spicy():
   spicy_receive = request.form['spicy_give']

   target_food = db.foods.find_one({'맵기': spicy_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'맵기': spicy_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '질문 2로 가주세요!'})


@app.route('/pref4', methods=['POST'])
def like_soup():
   soup_receive = request.form['soup_give']

   target_food = db.foods.find_one({'국물': soup_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'국물': soup_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '음식을 확인해주세요!'})


@app.route('/pref5', methods=['POST'])
def unlike_soup():
   soup_receive = request.form['soup_give']

   target_food = db.foods.find_one({'국물': soup_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'국물': soup_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '음식을 확인해주세요!'})


@app.route('/pref6', methods=['POST'])
def like_noodle():
   noodle_receive = request.form['noodle_give']

   target_food = db.foods.find_one({'면': noodle_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'면': noodle_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '음식을 확인해주세요!'})


@app.route('/pref7', methods=['POST'])
def unlike_noodle():
   noodle_receive = request.form['noodle_give']

   target_food = db.foods.find_one({'면': noodle_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'면': noodle_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '음식을 확인해주세요!'})


@app.route('/pref8', methods=['POST'])
def like_alcohol():
   alcohol_receive = request.form['alcohol_give']

   target_food = db.foods.find_one({'술': alcohol_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'술': alcohol_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '음식을 확인해주세요!'})


@app.route('/pref9', methods=['POST'])
def unlike_alcohol():
   alcohol_receive = request.form['alcohol_give']

   target_food = db.foods.find_one({'술': alcohol_receive})
   current_rank = target_food['누적']

   new_rank = current_rank + 1

   db.foods.update_many({'술': alcohol_receive}, {'$set': {'누적': new_rank}})
   return jsonify({'result': 'success', 'msg': '음식을 확인해주세요!'})


@app.route('/reset', methods=['POST'])
def refresh_foods():
   db.foods.update_many({'맵기': 'y'}, {'$set': {'누적': 0}})
   db.foods.update_many({'맵기': 'n'}, {'$set': {'누적': 0}})
   return jsonify({'result': 'success', 'msg': '새로고침 완료!'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)