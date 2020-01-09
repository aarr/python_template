#============================
# 基本
#============================
# 変数
# 英数＋アンダーバーのみ。数字から始まらない。
# 大文字、小文字の区別あり。
# 小文字始まり。スネークケース（hoge_fuga）
num = 10
string = "10"
sTring : string = "11" # 明示的に型宣言をしたい場合
null = None

# 型変換
print("＞型変換---------------")
print(str(num))        # 文字列変換
print(int(sTring))     # 整数変換
print(float(string))   # 浮動小数点数に変換

# 標準入力からの入力
print("＞標準入力---------------")
print("なにか入力してください。")
input_str = input()
print("「" + input_str + "」" + str(len(input_str)) + "文字入力されました。")

# Bool演算子／not演算子
# and/or、notを利用する
# 0、空文字
print("＞Bool演算子---------------")
if True and False :
    print("True and False")
elif False or False:
    print("False or False")
elif not True :
    print("not True")
else :
    print("and other")
# 0、None、空文字などはFalse
print("＞Bool値---------------")
if null :
    print("None")
elif 0 :
    print("0")
elif "" :
    print("empty")
elif 1 :
    print("1")
else :
    print("other")

# ループ文
# continue/breakの利用可能
print("＞ループ文；while---------------")
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
print("合計：" + str(sum_all))
print("奇数合計：" + str(sum_odd))

print("＞ループ文；for---------------")
# range()で繰り替えしを実行。
# 引数は１〜３つまで指定可能。開始、終了、ステップ数
for i in range(3) :
    print("for count:" + str(i))
for i in range(10, 13) :
    print("for count:" + str(i))
for i in range(100, 130, 10) :
    print("for count:" + str(i))

# import
# import moduleName1, moduleName2, moduleName
print("＞import---------------")
import random
print("ランダム値：" + str(random.randint(1, 10)))
# from moduleName import functionName(*指定可能)
# moduleNameを省略して呼び出すことが可能。module名が記載されている方がわかりやすいのでimport飲みの方がよい
print("＞from import---------------")
from random import *
print("ランダム値：" + str(randint(1, 10)))

# プログラム終了
print("＞プログラム終了---------------")
import sys
sys.exit()
print("ここにはたどり着かない")
