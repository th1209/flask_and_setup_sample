## このリポジトリの概要
* [Pythonプロフェッショナルプログラミング](https://www.amazon.co.jp/Python%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E7%AC%AC2%E7%89%88-%E3%83%93%E3%83%BC%E3%83%97%E3%83%A9%E3%82%A6%E3%83%89/dp/479804315X)2章・3章の写経。
* 以下2技術の調査用
  * Flask(軽量webフレームワーク)
  * setup.py(PyPIへの登録と、依存ライブラリの解決に使うスクリプト)

## 使い方
* python3、pip、virtualenvが必要。
* 以下2つの方法いずれかで、簡単なwebアプリ(ただの掲示板)が立ち上がる。

### 1.ソースをそのまま落として使う方法
* このリポジトリをgitcloneする
* `virtualenv (仮想環境名)`
* `source (仮想環境名)/bin/activate`
* pip install Flask
* `cd guestbook`
* `python3 __init__.py`
* webブラウザで ローカルホストの8000番へアクセス

### 2.setup.pyを使って、独立したパッケージとして落とす方法
* このリポジトリをgitcloneする
* `virtualenv (仮想環境名)`
* `source (仮想環境名)/bin/activate`
* 適当なプロジェクトを作り、プロジェクトの直下にcd
* `pip install (相対 or 絶対パス)/flask_and_setup_sample`
* `guestbook`

