:orphan:

pipenv
======================================

概要
---------------------------
ライブラリの依存関係を扱うツール
Pipfileというパッケージを管理するファイル
Pipfile.lockという依存関係を管理するファイル
で定義される


#. その他競合ツール

    * Poetry
        パッケージングする際に記述していた、setup.pyやsetup.cfg、MANIFEST.inなども
        １つのファイル（pyproject.toml）に記載することができる

    * Pyflow
        Pipenv/PoetryがPyenv＋venvで１つのPythonバージョン、仮想環境を管理するのに対して
        単体で複数のPythonのバージョンを管理し、指定のバージョンで仮想環境を作ることが可能。
        RUSTで実装されている、パフォーマンスや言語普及の観点から懸念あり。

    * distutils, setuptools, pip
        distutilsは標準パッケージに用意されたパッケージングツール
        distutilsを拡張したsetuptools。人気を博した。PyPAにより開発された。
        またPyPAにより、setuptoolsを拡張したpipが開発され、デファクトとなった。
        


設定
---------------------------
#. Pipfile作成

    .. code-block:: bash
        :caption: パッケージインストール時に、Pipfileに情報を保存

        $ pipenv install requests  # pip installと完全に互換性あり

    ただし.setup.pyを用意している場合、その中でimportしているライブラリを先にinstallしないとlock Faildでエラーとなる

#. 実行

    .. code-block:: python
        :caption: main.py（インストールしたパッケージを利用したスクリプト）

        import requests

        response = requests.get('https://httpbin.org/ip')
        print('Your IP is {0}'.format(response.json()['origin']))
    
    .. code-block:: bash
        :caption: 実行

        # runは仮想環境を有効にして、実行を行う
        $ pipenv run python main.py

        # もしくは下記のように、
        # 仮想環境を有効にする、pythonの実行、を分けて実行も可能
        $ pipenv shell
        (package) $ python main.py
        # 仮想環境を無効にする
        (package) $ exit

#. 既存Pipfile、Pipfile.lockを利用した環境構築

    .. code-block:: bash
        :caption: 最新バージョンを取得：Pipfileのpackagesで定義されている最新バージョンをインストール

        $ pipenv install         # パッケージ名を未指定
        $ pipenv install --dev   # 特定ステージング用のpackages定義をインストール

        # Pipfileに指定のPythonバージョンが存在しない場合、Pythonを指定
        $ pipenv install --python PATH  
    
    .. code-block:: bash
        :caption: 特定バージョンを取得：Pipfile.lockに記載されているバージョンをインストール

        $ pipenv sync

#. パッケージのバージョンアップ

    .. code-block:: bash
        :caption: 変更のあったパッケージを確認する

        $ pipenv update --outdated
    
    .. code-block:: bash
        :caption: パッケージの更新

        $ pipenv update                 # 全パッケージ
        $ pipenv update <package_name>  # 特定パッケージのみ

#. ステージング毎のパッケージ管理

    .. code-block:: bash
        :caption: 検証環境のみインストールしたい場合

        $ pipenv install --dev pytest 

    .. code-block:: text
        :caption: Pipfile

        [dev-packages]
        pytest = "*"
        
        [packages]
        requests = "*"

    Pipfileのpackagesがdev用として別で定義される

#. スクリプト登録/実行

    .. code-block:: text
        :caption: Pipfile：スクリプトを登録しておくことが可能

        [scripts]
        start = 'python main.py'
        test = 'pytest -v'
    
    .. code-block:: bash
        :caption: 実行

        $ pipenv run start
        $ pipenv run test


#. 仮想環境関連

    .. code-block:: bash
        :caption: 仮想環境のパス確認

        $ pipenv --venv
        # ~/.local/share/virtualenves/以下に作られる
    
    .. code-block:: bash
        :caption: 仮想環境のパスを変える

        $ export WORKON_HOME=~/venvs
        $ pipenv install package_name
    
    .. code-block:: bash
        :caption: プロジェクト毎に仮想環境を作る

        $ export PIPENV_VENV_IN_PROJECT=true 
        $ pipenv install    # カレントディレクトリに.venvが作成される
    
    .. code-block: bash
        :caption: 仮想環境を削除

        $ pipenv --rm



使い方
---------------------------
#. バージョン管理対象
    #. Pipfile
    #. Pipfile.lock
        複数のPythonバージョンで利用する場合には、バージョン管理対象外とする


トピック
---------------------------
* Pipfile or setup.py


パッケージング
---------------------------
* `パッケージングの歴史 <https://engineer.recruit-lifestyle.co.jp/techblog/2019-12-25-python-packaging-specs/>`_
* パッケージング形式
    #. bdist
        PyPAにより、wheelが開発され、配布側はwheel形式にファイルをまとめ、利用者側はダウンロードして展開するだけ。
        ファイル形式としてのwheelと、それを作るライブラリとしてのwheelを混同しがちなので気をつける。

    #. sdist (source distribution)
        利用者側がsetup.pyを実行して、bdist形式のパッケージを作成して、インストールする形式

* パッケージング方法
    .. code-block:: bash
        :caption: bdist

        $ pipenv install wheel
        $ python setup.py bdist_wheel

    .. code-block:: bash
        :caption: sdist

        $ pytyon setup.py sdist

    
    いずれにせよ、setup.pyは自身で作成する必要がある。  

    .. code-block:: python
        :caption: サンプル

        from setuptools import setup

        requires = ["requests>=2.14.2"]

        setup(
            name='your_package',
            version='0.1',
            description='Awesome library',
            url='https://github.com/whatever/whatever',
            author='yourname',
            author_email='your@address.com',
            license='MIT',
            keywords='sample setuptools development',
            packages=[
                "your_package",
                "your_package.subpackage",
            ],
            install_requires=requires,
            classifiers=[
                'Programming Language :: Python :: 3.6',
            ],
        )
