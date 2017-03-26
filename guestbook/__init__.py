# coding: utf-8
import shelve
from datetime import datetime
from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

# デフォルトで使うファイル
DATA_FILE = 'guestbook.dat'


def save_data(name, comment, create_at, save_to=DATA_FILE):
    """
    投稿データを、ファイルに書き込む
    """
    database = shelve.open(save_to)
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })
    database['greeting_list'] = greeting_list
    database.close()


def load_data(load_from=DATA_FILE):
    """
    ファイルから、投稿データを取得する
    """
    database = shelve.open(load_from)
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list


@application.route('/')
def index():
    """
    テンプレートを出力する 。
    """
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)


@application.route('/post', methods=['POST'])
def post():
    """
    投稿を保存し、リダイレクトする。
    """
    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = datetime.now()
    save_data(name, comment, create_at)

    return redirect('/')


@application.template_filter('nl2br')
def nl2br_filter(s):
    """
    改行をbrタグに変換するフィルタ。
    """
    return escape(s).replace('\n', Markup('</br>'))


@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    """
    datetimeを表示用にフォーマットするフィルタ。
    """
    return dt.strftime('%Y%m%d %H:%M:%S')


def main():
    """
    setup.pyでパッケージインストール後、
    対応するコマンドが実行された時に呼ばれる関数。
    """
    application.run('127.0.0.1', 8000)

# このスクリプトを直接叩いた場合、以下処理が呼ばれる
if __name__ == '__main__':
    application.run('127.0.0.1', 8000, debug=True)









