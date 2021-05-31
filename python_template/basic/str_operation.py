#!/usr/bin/env python3
# str_operation.py
#

""" 文字列操作
文字列操作サンプル集
"""
import pyperclip

import com.console

log = com.console.log
log_add_line = com.console.log_add_line

# シングルクォーテーション、ダブルクォーテーションいずれでもよい
log('#============================')
log('# 文字列操作')
log('#============================')
# エスケープ文字 +++++++++++++++++++++++
log("＞エスケープ文字 ---------------")
log('バックスラッシュ(\\)がエスケープ文字')
log(' └ シングルクォーテーション:\', ダブルクォーテーション:\", tab:\t, 改行:\n バックスラッシュ:\\')
log_add_line(1)

# raw文字列 +++++++++++++++++++++++
# r'xxxx' のように記載。raw文字列ではエスケープが不要
log("＞raw文字列 ---------------")
log(r'raw文字列：シングルクォーテーション:\', ダブルクォーテーション:\", tab:\t, 改行:\n バックスラッシュ:\\')
log_add_line(1)

# 複数行文字列 +++++++++++++++++++++++
"""
複数行コメント
複数行コメント
"""
log("＞複数行文字列（\'\'\'で括る） ---------------")
log('''1行目
2行目
3行目''')
log_add_line(1)

# 便利メソッド +++++++++++++++++++++++
log("＞便利メソッド ---------------")
string = 'Hello world'
log('ORIGINAL', string)
log('UPPER', string.upper())
log('LOWER', string.lower())
log('IS UPPER', str(string.isupper()))
log('IS LOWER', str(string.islower()))
log('IS ALPHA', str('abcABC'.isalpha()))
log('IS ALPHA/NUMBER', str('abc123'.isalnum()))
log('IS DECINAL', str('123'.isdecimal()))
log('IS SPACE', str('    '.isdecimal()))
log('IS TITLE', str(string.istitle()))
log('START WITH', str(string.startswith('HELLO')))
log('END WITH', str(string.endswith('hello')))
# 文字列結合、分割
string_join = ', '.join(['I', 'am', 'hungury'])
log('JOIN', string_join)
log('SPLIT', string_join.split(','))
# 固定長変換
# 左右どちらにスペースを入れるべきか指定が可能
log('RJUST', string.rjust(30, '-'))
log('LJUST', string.ljust(40, '+'))
log('CENTER', string.center(20, '='))
# トリム
# 引数で指定された文字列h,oを両端、右側、左側から削除する
string_strip = 'hoge 123 deackau 83dk egoh'
log('STRIP', string_strip.strip('ho'))
log('RSTRIP', string_strip.rstrip('hoge'))
log('LSTRIP', string_strip.lstrip('hoge'))
# format
string_format = '{0} is {1}'
log('FORMAT', string_format.format('123', 'number'))
# クリップボード
pyperclip.copy('CLIPBOARD COPY')
log('CLIPBOARD PASTE', pyperclip.paste())
log_add_line()
