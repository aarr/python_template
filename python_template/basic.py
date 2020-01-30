#============================
# 基本
#============================
from console import *
#
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
indent()


# 標準入力からの入力 +++++++++++++++++++++++
# 複数の入力を受け付けるのであれば、inputを繰り返し実装するのではなく
# ループして、入力内容をリストに保持するのがよい。
log("＞標準入力---------------")
log("なにか入力してください。")
input_str = input()
log("「" + input_str + "」" + str(len(input_str)) + "文字入力されました。")
indent()


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
indent()


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
indent(1)

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
indent()


# import +++++++++++++++++++++++
# import moduleName1, moduleName2, moduleName
log("＞import---------------")
import random
log("RANDOM", random.randint(1, 10))
indent(1)

# from moduleName import functionName(*指定可能)
# moduleNameを省略して呼び出すことが可能。module名が記載されている方がわかりやすいのでimport飲みの方がよい
log("＞from import---------------")
from random import *
log("RANDOM", randint(1, 10))
indent()


# コンテナ型  +++++++++++++++++++++++
import container


# 関数  +++++++++++++++++++++++
import function 


# 文字列操作  +++++++++++++++++++++++
import str_operation


# プログラム終了 +++++++++++++++++++++++
log("＞プログラム終了---------------")
import sys
sys.exit()
log("ここにはたどり着かない")

