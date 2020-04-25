#!/usr/bin/env python3
# basic.py

import sys, os, time

# 別ディレクトリのため、パス追加
script_dir = os.path.abspath(__file__)
base_dir = os.path.join(os.path.dirname(script_dir), '..', 'python_template')
sys.path.append(os.path.join(base_dir, 'com'))

import console 
from performance import Performance
from file_manager import *

""" Pythonサンプル
Python基本実装集
"""

# performance.pyテスト
performance = Performance()
performance.mark('hoge:start')
time.sleep(2)
performance.mark('hoge:end')
performance.mesure('hoge', 'hoge:start', 'hoge:end')
log(performance.get_entry('hoge'))
log(performance.get_simple_entries())



# 関数の中の変数は関数内でのみ有効であとは確認できる。。。
def func(min, max, roop_count):
    if roop_count < 5:
        container = {}
        for num in range(min, max):
            container[num] = min * max
        
        log('MIN:{0}, MAX:{1}'.format(min, max), container)
        func(min * 2, max * 2, roop_count + 1)
    else:
        return

func(1,3, 0)