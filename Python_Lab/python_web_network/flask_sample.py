"""
#############################################################################
flask:webフレームワーク
・ディレクトリによるページ切り替え
・URLに値を入れ、その値を動的にWebページに反映させる
・POSTなののリクエストの処理
・DBとの接続(HTTPメソッドに応じた処理の記述)
#############################################################################
"""
import sqlite3

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

# DBへ接続する（接続があればg(グローバル)から引っ張ってくるが、なければ接続する）
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_flask_sqlite.db')
    return db

# APPを終了するときはDB接続をクローズする
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    # DB接続（personテーブルが存在しない場合は作成する）
    db = get_db()
    curs = db.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS persons('
                 'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    db.commit()
    
    name = request.values.get('name', name)
    # GETリクエストの場合
    if request.method == 'GET':
        curs.execute('SELECT * FROM persons WHERE name ="{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return '{}:{}'.format(user_id, name), 200
    
    # POSTリクエストの場合
    if request.method == 'POST':
        curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
        db.commit()
        return 'created {}'.format(name), 201
    
    # PUTリクエストの場合
    if request.method == 'PUT':
        new_name = request.values['new_name']
        curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(new_name, name))
        db.commit()
        return 'updatas {}:{}'.format(name, new_name), 200
    
    # DELETEリクエストの場合
    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
        db.commit()
        return 'deleted {}'.format(name), 200
    
    
@app.route('/')
def hello_top():
    return 'top paga now!!'

@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world2(username=None):
    # return 'hello world! {}'.format(username)
    
    # htmlのテンプレートで返す場合は下記
    # ※注意：テンプレートはこのプログラムと同一階層に「templetes」フォルダ配下に入れる
    return render_template('hello.html', username=username)

@app.route('/post', methods=['POST'])
def show_post():
    return str(request.values['username'])
                    
def main():
    app.debug = True
    app.run()
    # default setting
    # app.run(host='127.0.0.1', port=5000)
    
if __name__ == '__main__':
    main()

