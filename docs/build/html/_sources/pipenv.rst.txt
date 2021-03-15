:orphan:

pipenv
======================================

設定
---------------------------
#. Pipfile作成

    .. code-block:: bash
        :caption: パッケージインストール時に、Pipfileに情報を保存

        $ pipenv install requests  # pip installと完全に互換性あり
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

