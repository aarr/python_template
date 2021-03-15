パッケージ
======================================

構成
---------------------------

 | 複数のモジュールを集約したディレクトリのことをパッケージと呼ぶ
 | モジュール＝ファイル、パッケージ＝ディレクトリ
 | パッケージには必ず「__init__,py」が必要になる
 | 以下の構成で、下記コマンドにてパケージを実行することが可能
 | __main__.pyが実行される為、

.. code-block:: bash
   :caption: 実行コマンド
   :name: execute_package

   # パッケージ実行
   $ python ./src/my_package_name

   # テスト実行
   $ pytest -v

.. code-block:: text
   :caption: 標準のパッケージ構成。今回のケースだとsrcフォルダはなくてもよい。

    my_package_name
    |- README.rst
    |- LICENCE
    |---src                    <- モジュール名に重複がある場合にsrcフォルダを挟むことが推奨されている。
    |   |- my_package_name     <- ソースを配置。単一モジュールであれば、ルート直下への配置でもよい。
    |       |- __main__.py     <- パッケージ実行された際に呼ばれるスクリプト
    |       |- __init__.py     <- Pythonパッケージとして認識されない。importできない
    |       |---mod1
    |       |   |- __init__.py <- Pythonパッケージとして認識されない。importできない
    |       |   |- main.py
    |       |
    |       |---mod2
    |           |- __init__.py <- Pythonパッケージとして認識されない。importできない
    |           |- sub1.py
    |           |- sub2.py
    |
    |---tests
    |   |---mod1
    |       |- __init__.py     <- Pythonパッケージとして認識されない。テストモジュールとして認識されない
    |       |- test_main.py
    |
    |---docs                   <- sphinxで生成するドキュメント（後述）
        |- Makefile
        |- make.bat
        |---build
        |   |- index.html
        |
        |---source
            |- index.rst


シンボリックテーブル
---------------------------

 | モジュールはそれぞれプライベートなシンボルテーブルを保持している。
 | モジュールでは、これをグローバルなシンボルテーブルとして使用する。
 | その為、他モジュールとグローバル変数の競合は発生しない。


インポート
---------------------------
 | インポートとは、自身のシンボリックテーブルに、インポートしたモジュールのシンボリックテーブルを取り込むということである。
 | パッケージ名までのインポートは、そのパッケージ（ディレクトリ）の「__init__.py」を読み込むことになる。
 | 仮に「__init__.py」に何も記載されていない場合、インポートしても何も取り込まれない。
 | モジュール名までインポートする場合、そのモジュール内の関数を読みこむことになる。
 | 「__init__.py」を実装することで、パッケージをインポートするだけでパッケージ内のモジュールをインポートできる。

 .. code-block:: python

   from module import *           # moduleの「_」始まり以外の定義をすべて取り込む
   from module import func as mf  # 取り込む名称を変えることも可能


インポートの種類
---------------------------

#. 暗黙的な相対インポート
#. 明示的な相対インポート
#. 絶対インポート

.. code-block:: python
   :caption: 暗黙の相対インポート例：my_package_name/mod1/main.py

    import ..mod2.sub1
    
.. code-block:: python
   :caption: 明示的な相対インポート例：my_package_name/mod2/sub1.py

    from . import sub2

.. warning::
   トップレベルでパッケージとして実行された際（:ref:`execute_package`）には
   正しく動作するが、moduleとして実行された場合にはエラーとなる。
   「.」が認識されるディレクトリが変わる為

.. code-block:: python
   :caption: 絶対インポート例：my_package_name/mod2/sub1.py

    import my_package_name.mod2.sub2


モジュール検索パス
---------------------------
 | Pythonではモジュールを検索する際に下記の順序で検索を行う。

 #. ビルドインモジュール（Pythonに最初から組み込まれているモジュール）
 #. sys.path

   | 下記の内容で初期される
   | 1. sys.pathで指定されているディレクトリ
   | 2. PYTHONPATH
   | 3. インストールごとのデフォルト（実行されるPythonスクリプトのディレクトリ）

   .. code-block:: python
      :caption: 編集可能（追加の例）

      sys.path.append(add_path)


.. _vertual-env-label:

仮想環境
---------------------------
 | pipenvをメインで利用し、必要ならdirenvも利用。
 | 直接触らないが、裏ではvenvが利用されている。

* venv

 | 複数の開発を行っている際に、異なるバージョンのパッケージを利用したい場合、仮想環境を分けることでその実現が可能
 | 仮想環境名はディレクトリ名となる。下記の例であれば、カレントディレクトリの名称が仮想環境名となる。

   .. code-block:: bash
      :caption: カレントディレクトリに仮想環境を構築

      $ python -m venv .

   .. code-block:: bash
      :caption: 有効化

      $ source ./bin/activate

   .. code-block:: bash
      :caption: デフォルトに戻す

      (カレントディレクトリ) $ deactivate

* pipenv

 | pip（パッケージの管理）とvenv（仮想環境）の機能をあわせて提供している（ラップしている）
 | :doc:`詳細<pipenv>`
 | `本家開発フロー <https://pipenv-ja.readthedocs.io/ja/translate-ja/>`_


* direnv

 | venvにおけるactivate/deactivateを自動で行うためのツール
 | 特定のフォルダに移動した際に、環境変数を行う。
 | `direnv <https://direnv.net>`_

テスト
---------------------------

* unittest

 | テストスクリプトの命名規約に合わせ、unittestをモジュール実行（オプションｍ）することでテスト実行可能
 | オプションm：sys.pathから指定されたモジュールを探し、__main__モジュールとして実行
 | 実行時にはテスト対象パッケージのトップレベルディレクトリで実行する（sys.pathに追加されるので）

 | テストスクリプトは「test_script.py」とする
 | テストス関数名は「test_func」とする

   .. code-block:: bash
      :caption: テスト実行

      $ python -m unittest discover

   .. code-block:: python
      :caption: test_main.py

      import unittest
      import my_package_name.main as target

      class TestMain(unittest.TestCase):

         def setUp(self):
            """初期処理"""
            self.func = target
         
         def test_1(self):
            """テスト内容"""
            self.asserTrue(self.func())

         def tearDown(self):
            """終了処理"""
            self.func = None 

* pytest

 | 最も利用されているテストフレームワーク
 | テスト用関数命名規約に従うことで、自動でテスト対象を検索し、実行してくれる
 | サンプルは下記
 | `pipenv_test <https://github.com/aarr/pipenv_test>`_

   * 特徴

   #. PATHにルートディレクトリが追加される
   #. fixutureを利用することで、setup/teardownの様な実装も可能
   #. fixutureの実行スコープを定義可能（テスト全体、モジュール単位、メソッド単位など）
   #. 同階層、サブ階層で共通利用可能なfixuture定義として、conftest.pyに実装可能
   #. 全テストケースで必ず実行するfixutureはメソッド毎に定義を追加しなくても、iniファイルに記載が可能


その他
======================================

sphinx(reStructuredText)
---------------------------

 * install

 .. code-block:: bash
   :caption: sphinxのinstall

   $ pip3 install sphinx

 .. code-block:: bash
   :caption: sphinx-quickstartのinstall確認

   $ which sphinx-quickstart
   $ sphinx-quickstart --version

 .. code-block:: bash
   :caption: ドキュメント作成

   $ sphinx-quickstart documentName
   # sphinx-quickstart docs
   # これでdocsディレクトリが作成され、その中にrstファイルからhtmlを作成する為のスクリプト等が生成される


 * rstファイル->html生成

   .. code-block:: bash
      :caption: docsフォルダにて実行（index.rstを編集）

      $ make html
      # html以外も生成可能。


AWS lambda
---------------------------
 | venvを利用し、必要なパッケージのみを抽出できるようにする。
 | 独自実行したlambda_hanlderをそれらに加え、zipファイルとしてUpload

   #. :ref:`vertual-env-label` 構築
   #. 必要モジュールのinstall

      .. code-block:: bash

         $ ./bin/activate
         (my_package_name) $ pip3 install package_name
         (my_package_name) $ deactivate
   #. zipファイルに纏める

      .. code-block:: bash
         :caption: my_package_nameディレクトリ直下で実行

         $ zip -r9 ./function.zip ./lib/python3.8/site-packages
   #. lambda_handlerの追加

      .. code-block:: bash
         :caption: my_package_nameディレクトリ直下で実行

         $ zip -g ./function.zip ./lambda_hanlder.py
   #. awc-cli、もしくはGUIにてアップロード

      .. code-block:: bash
         :caption: aws-cliの場合

         $ aws lambda update-function-code --function-name lambda_hander_name --zip-file fileb://function.zip


Coding
---------------------------
 | Pythonのコーディングについて
 | :doc:`Coding<coding>`
