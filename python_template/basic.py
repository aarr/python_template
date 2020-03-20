#!/usr/bin/env python3
# basic.py
# 

""" Pythonサンプル
Python基本実装集
"""

from console import *
import datetime
log('+++++++++++++++++++ START +++++++++++++++++++')
log('#============================')
log('# 基本')
log('#============================')
# 変数
# 英数＋アンダーバーのみ。数字から始まらない。
# 大文字、小文字の区別あり。
# 小文字始まり。スネークケース（hoge_fuga）
num = 10
string = "10"
sTring : string = "11" # 明示的に型宣言をしたい場合
null = None

# 型変換 +++++++++++++++++++++++
log("＞型変換---------------")
log(str(num))        # 文字列変換
log(int(sTring))     # 整数変換
log(float(string))   # 浮動小数点数に変換
log_add_line()

# 型判定 +++++++++++++++++++++++
log('＞型、インスタンス判定')
log('TYPE', int == type(100))
# いずれかに一致するか
log('TYPE(MULTI)', type(100) in (str, float))

log('IS INSTANCE', isinstance('TEST', str))
# いずれかに一致するか
log('IS INSTANCE(MULTI)', isinstance(100, (str, float)))

# 標準入力からの入力 +++++++++++++++++++++++
# 複数の入力を受け付けるのであれば、inputを繰り返し実装するのではなく
# ループして、入力内容をリストに保持するのがよい。
log("＞標準入力---------------")
print("なにか入力してください。")
input_str = input()
log("「" + input_str + "」" + str(len(input_str)) + "文字入力されました。")
log_add_line()


# Bool演算子／not演算子 +++++++++++++++++++++++
# and/or、notを利用する
# 0、空文字
log("＞Bool演算子---------------")
if True and False :
    log("True and False")
elif False or False:
    log("False or False")
elif not True :
    log("not True")
else :
    log("and other")
# 0、None、空文字などはFalse
log("＞Bool値---------------")
if null :
    log("None")
elif 0 :
    log("0")
elif "" :
    log("empty")
elif 1 :
    log("1")
else :
    log("other")
log_add_line()

# 日付
log("＞日付---------------")
now = datetime.datetime.now()
formatted_now = now.strftime('%Y%m%d_%H%M%S')
log('NOW', formatted_now)
log_add_line(1)

# ループ文 +++++++++++++++++++++++
# continue/breakの利用可能
log("＞ループ文；while---------------")
count = 0
sum_all = 0
sum_odd = 0
while count <= 100 :
    if count > 10 :
        break
    sum_all = sum_all + count 

    if count%2 == 0 :
        count = count + 1
        continue
    sum_odd = sum_odd + count 
    count = count + 1
log("SUM", sum_all)
log("ODD SUM", sum_odd)
log_add_line(1)

log("＞ループ文；for---------------")
# range()で繰り替えしを実行。
# 引数は１〜３つまで指定可能。開始、終了、ステップ数
for i in range(3) :
    log("FOR COUNT", i)
for i in range(10, 13) :
    log("FOR COUNT", i)
for i in range(100, 130, 10) :
    log("FOR COUNT", i)
# dictを利用したfor文
# iteratorを３種類選択可能。keys,values,items
dict_for_sample = {'hoge' : '10', 'fuga' : '20', 'fage' : '30'}
for key  in dict_for_sample.keys() :
    log('DICT CONTENT', 'KEY:' + key + ', VALUE:' + dict_for_sample[key])
log_add_line()


# import +++++++++++++++++++++++
# import moduleName1, moduleName2, moduleName
log("＞import---------------")
import random
log("RANDOM", random.randint(1, 10))
log_add_line(1)

# from moduleName import functionName(*指定可能)
# moduleNameを省略して呼び出すことが可能。module名が記載されている方がわかりやすいのでimport飲みの方がよい
log("＞from import---------------")
from random import *
log("RANDOM", randint(1, 10))
log_add_line()

# 例外処理
log("＞例外処理 ---------------")
# 割り算（サンプル関数）
import traceback
def divide(arg1, arg2) :
    result = None
    try:
        result =  arg1 / arg2 
    # except 例外 as 変数名: とし、発生した例外を利用することが可能
    # exceptを続けていくことで、複数のエラーハンドリングが可能
    except ZeroDivisionError as error:
        log("ERROR(ZeroDivision)", error)
        # stacktraceを出力
        # Exceptionは握りつぶして、stacktraceだけをログ出力する際に利用
        log(traceback.format_exc())
    # Exceptionを明示的に定義しないと、全ての例外を補足する。
    except:
        log("ERROR", error)
    # 例外が発生しなかった場合の処理を記述可能
    else:
        return result
    # 必ず実行する
    finally:
        log("FINALLY RESULT", result)

log("10 / 3 = ", divide(10, 3))
log_add_line(1)
log("10 / 0 = ", divide(10, 0))   # エアーメッセージが表示され、戻り値としてはNoneとなる
log_add_line()


# コンテナ型  +++++++++++++++++++++++
import container

# 関数  +++++++++++++++++++++++
import function 

# 文字列操作  +++++++++++++++++++++++
import str_operation

# 正規表現  +++++++++++++++++++++++
import regex

# ファイル操作  +++++++++++++++++++++++
import file_operation 
file_operation.main()

import file_control

# ファイル操作  +++++++++++++++++++++++
# import web_scraping


# プログラム終了 +++++++++++++++++++++++
log('+++++++++++++++++++ END +++++++++++++++++++')
import sys
sys.exit()
log("ここにはたどり着かない")

