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
# 複数の入力を受け付けるのであれば、inputを繰り返し実装するのではなく
# ループして、入力内容をリストに保持するのがよい。
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


# リスト
print("＞リスト ---------------")
list_first_half = ["1", "2", "3", "4", "5"]
list_second_half = ["6", "7", "8", "9", "10"]

print("２要素目 : " + list_first_half[1])
# indexのマイナス指定は最終項目からのカウントとなる
print("最終項目 : " + list_first_half[-1])
# ＞範囲指定
# X:Y -> Xは含む。Yは含まない。いずれも省略可能
list_part = list_first_half[1:3]
print("要素数 : " + str(len(list_part))) 
print("切出要素 : ", list_part[0], list_part[1], sep=",")
# ＞リスト連結
list_sum = list_first_half + list_second_half
print("リスト連結 : ", end="")
print(list_sum)
# ＞リスト増幅
list_tripple = list_sum * 3
print("リスト３倍 : ", end="")
print(list_tripple)
# ＞要素削除
# delは変数の削除にも利用できるが、殆どの場合リストの要素削除に使われる
print("3倍リストサイズ : " + str(len(list_tripple)))
del list_tripple[10:] # 10要素以降を削除
print("3倍リストサイズ（削除後） : " + str(len(list_tripple)))
# 要素存在確認（in / not in）
contains_1 = "1" in list_first_half
print("１が含まれているか : " + str(contains_1))
contains_num1 = 1 in list_first_half
print("数字１が含まれているか : " + str(contains_num1)) # 型が異なると含まれないと判断される
contains_1 = "6" in list_first_half
print("６が含まれているか : " + str(contains_1))
# ＞変数への複数代入法
# リストのサイズと、変数の個数が同じであること
# それが異なる場合、エラーとなる
list_sample = ["one", "two", "three"]
list_arg1, list_arg2, list_arg3 = list_sample
print("複数代入法 : ", list_arg1, list_arg2, list_arg3)
try:
    error_arg1, error_arg2 = list_sample
except ValueError as exception:
    print("複数代入エラー : ", end="")
    print(exception)
# ＞リスト提供メソッド
list_sum.append("11")           # 操作対象のリストに要素を追加する
list_sum.extend(["0", "-10"])   # + の場合、コピーされ新たなリストが作成される。extendは操作対象のリストに指定されたリストを追加する 
list_sum.remove("1")            # delは要素番号を指定して削除、removeは要素値を指定して削除
print("2は何番目に存在するか : " + str(list_sum.index("2")))
print("操作後リスト : ", list_sum)
print("8は何番目に存在するか（5 - 10の間） : " + str(list_sum.index("8", 5, 10)))
list_sum.sort()
print("操作後リスト（ソート）", list_sum)
# ＞リスト風（文字列）
# リストはミュータブルだが、文字列はイミュータブル（不変）
str_like_list = "123"
print(str_like_list, "-> 2文字目 : ", str_like_list[1])
# ＞リスト風（タプル）
# 文字列同様イミュータブル（不変）
def editList(target, index, value) :
    try:
        target[index] = value
    except TypeError as exception : 
        print("更新エラー : ", end="")
        print(exception)
    else :
        print("更新完了 : ", target)

tuple_like_list = (12, "34", None)
print(tuple_like_list, " -> 3要素目 : ", tuple_like_list[2])
editList(tuple_like_list, 0, "X")
# ＞リスト、タプルへの型変換
# タプリを更新したい場合に、リストに変換して操作する
# 更新させたくないリストをタプルにするのもあり。
# しかしタプルにすると利用できるメソッドが異なるのでまたリストする必要が出てくるケースもあるだろう
list_by_tuple = list(tuple_like_list)
editList(list_by_tuple, 0, "X")
tuple_by_list = tuple(list_sum)
editList(tuple_by_list, 0, "X")

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




