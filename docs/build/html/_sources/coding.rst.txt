Coding規約
======================================

import
---------------------------

* アルファベット順にする。更に下記の順で記述し、それぞれの間に１行間隔を開ける

#. 標準ライブラリ
#. サードパーティライブラリ
#. 自作ライブラリ
#. ローカルファイル


.. code-block:: python
   :caption: import順
   :name: import sample

   import collections
   import os
   import sys

   import termcolor

   import my_library

   import local_file

