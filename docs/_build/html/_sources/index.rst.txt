======================================
パッケージ
======================================
構成
 | 複数のモジュールを集約したディレクトリのことをパッケージと呼ぶ
 | モジュール＝ファイル、パッケージ＝ディレクトリ
 | パッケージには必ず「__init__,py」が必要になる

.. code-block:: text

    packageName
    |---packageName          <- パッケージのディレクトリ。ディレクトリ名＝パッケージ名
    |   |--- __init__.py     <- これがないとパッケージと呼ぶことはできない
    |   |--- hoge.py
    |   |      ┗--- funcA(n)
    |   ┗--- fuga.py
    |          ┗--- funcB(n)



インポート
 | パッケージ名までのインポートは、そのパッケージ（ディレクトリ）の「__init__.py」を読み込むことになる
 | 仮に「__init__.py」に何も記載されていない場合、インポートしても何も取り込まれない。
 | モジュール名までインポートする場合、そのモジュール内の関数を読みこむことになる。

 | 下記のように「__init__.py」を実装することで、パッケージをインポートするだけでパッケージ内の
 | モジュールをインポートできる
 | 下記の実装は **相対インポート** という。

.. code-block:: python
   :caption: __init__.py

    from . import hoge
    from . import fuga

モジュール検索パス
 | Pythonではモジュールを検索する際に下記の順序で検索を行う。

 1. ビルドインモジュール（Pythonに最初から組み込まれているモジュール）
 2. Pythonコマンドに渡した渡したファイルのある直下のディレクトリ直下

 下記の構成で、python main.pyと実行した際に、Pythonもジュールを検索しにいく場所は
 トップのpackageName以下である。そのため、どのソースにimport hogeと記載しても
 hoge.pyを見つけることはできない。
 相対インポートの場合、それを解決することが可能。

.. code-block:: text

    packageName
    |---packageName
    |   |--- __init__.py
    |   |--- hoge.py
    |   |      ┗--- funcA(n)
    |   ┗--- fuga.py
    |          ┗--- funcB(n)
    |--- main.py





======================================
その他
======================================

sphinx(reStructuredText)
==================================
 install

 * sphinxのinstall

 .. code-block:: bash

   pip3 install sphinx

 * sphinx-quickstartのinstall確認

 .. code-block:: bash

   which sphinx-quickstart
   sphinx-quickstart --version

 * ドキュメント作成

 .. code-block:: bash

   sphinx-quickstart documentName
   # sphinx-quickstart docs
   # これでdocsディレクトリが作成され、その中にrstファイルからhtmlを作成する為のスクリプト等が生成される


 * rstファイル->html生成

  | docsフォルダにて実行（index.rstを編集）

 .. code-block:: bash

   make html
   # html以外も生成可能。


