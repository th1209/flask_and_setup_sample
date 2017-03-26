from setuptools import setup
from setuptools import find_packages

setup(
    name='guestbook',
    version='1.0.0.',
    # 以下のようにすると、動的にパッケージを探してくれる(複数パッケージがあった場合に便利)。
    packages=find_packages(),
    # .py以外のファイルもインストールするか。以下の記載では足りず、MANIFEST.inで詳細な記載が必要になることに注意。
    include_package_data=True,
    # 以下に、依存しているパッケージを記載する。
    install_requires=[
        'Flask',
    ],
    # 以下のようにすると、guestbookというコマンドが作られ、guestbookパッケージ内の
    # __init__.pyに定義したmain関数が実行される。
    entry_points="""
        [console_scripts]
        guestbook = guestbook:main
    """,
)
