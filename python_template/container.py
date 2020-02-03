#============================
# コンテナ型
#============================
from console import *
# 複数のオブジェクトを格納できるデータ構造
# コンテナ型
#  └ シーケンス型（list, tuple, str）
#  └ 集合型（set, frozenset）
#  └ 辞書型（dict）
log('#============================')
log('# コンテナ型')
log('#============================')
# リスト +++++++++++++++++++++++
log("＞list(シーケンシャル型) ---------------")
list_first_half = ["1", "2", "3", "4", "5"]
list_second_half = ["6", "7", "8", "9", "10"]
log('ORIGINAL LIST1', list_first_half)
log('ORIGINAL LIST2', list_second_half)

log("LIST1 ELEM(2)",  list_first_half[1])
# indexのマイナス指定は最終項目からのカウントとなる
log("LIST1 ELEM(LAST)",  list_first_half[-1])

# ＞範囲指定
# X:Y -> Xは含む。Yは含まない。いずれも省略可能
list_part = list_first_half[1:3]
log("LIST1 CUT ELEM NUM",  str(len(list_part))) 
log("LSIT1 CUT ELEM(0,1)", list_part[0], list_part[1], sep=",")

# ＞リスト連結
list_sum = list_first_half + list_second_half
log("LIST JOIN", list_sum)

# ＞リスト増幅
list_tripple = list_sum * 3
log("LIST 3TIMES", list_tripple)

# ＞要素削除
# delは変数の削除にも利用できるが、殆どの場合リストの要素削除に使われる
log("LIST 3TIMES SIZE",  str(len(list_tripple)))
del list_tripple[10:] # 10要素以降を削除
log("LIST DEL AF DEL",  str(len(list_tripple)))
# 要素存在確認（in / not in）
contains_1 = "1" in list_first_half
log("CONTAINS str(1)",  str(contains_1))
contains_num1 = 1 in list_first_half
log("CONTAINS int(1)",  str(contains_num1)) # 型が異なると含まれないと判断される
contains_1 = "6" in list_first_half
log("CONTAINS str(6)",  str(contains_1))

# ＞変数への複数代入法
# リストのサイズと、変数の個数が同じであること
# それが異なる場合、エラーとなる
list_sample = ["one", "two", "three"]
list_arg1, list_arg2, list_arg3 = list_sample
log('LIST', list_sample)
log("MULTI ARGS", list_arg1, list_arg2, list_arg3)
try:
    error_arg1, error_arg2 = list_sample
except ValueError as exception:
    log("MULTI ARGS ERROR", exception)
log_add_line(1)

# ＞リスト提供メソッド
log("＞リスト提供メソッド ---------------")
list_sum.append("11")           # 操作対象のリストに要素を追加する
list_sum.extend(["0", "-10"])   # + の場合、コピーされ新たなリストが作成される。extendは操作対象のリストに指定されたリストを追加する 
list_sum.remove("1")            # delは要素番号を指定して削除、removeは要素値を指定して削除
log("WHAT NUM(2)",  str(list_sum.index("2")))
log("操作後リスト", list_sum)
log("WHAT NUM(8 :5 - 10)",  str(list_sum.index("8", 5, 10)))
list_sum.sort()
log("LIST SORTED", list_sum)

# ＞文字列
# リストはミュータブルだが、文字列はイミュータブル（不変）
log("＞str(シーケンシャル型) ---------------")
str_like_list = "123"
log(str_like_list, "ELEM(2):", str_like_list[1], title_sep=' -> ')
log_add_line(1)

# ＞タプル
# 文字列同様イミュータブル（不変）
log("＞tuple(シーケンシャル型) ---------------")
def editList(target, index, value) :
    try:
        target[index] = value
    except TypeError as exception : 
        log("ERROR UPDATE", exception)
    else :
        log("COMP UPDATE", target)

tuple_like_list = (12, "34", None)
log(tuple_like_list, "ELEM(3):", tuple_like_list[2], title_sep=' -> ')
editList(tuple_like_list, 0, "X")
log_add_line(1)

# ＞リスト、タプルへの型変換
# タプリを更新したい場合に、リストに変換して操作する
# 更新させたくないリストをタプルにするのもあり。
# しかしタプルにすると利用できるメソッドが異なるのでまたリストする必要が出てくるケースもあるだろう
log(' - 型変換(list<->tuple)')
list_by_tuple = list(tuple_like_list)
editList(list_by_tuple, 0, "X")
tuple_by_list = tuple(list_sum)
editList(tuple_by_list, 0, "X")
log_add_line()


# 辞書型（dict） +++++++++++++++++++++++
log("＞辞書型（dict） ---------------")
dict_sample = {'key1' : 1, 'key2' : 2, 'key3' : 3}
log('DICTIONARY', dict_sample)
log_add_line(1)

# ＞キー、値が含まれているかの確認
# 存在しないことの確認であれば、not inを利用すればOK
log(' - dict 存在確認')
isExistsKey = 'key1' in dict_sample.keys()
log("CONTAINS key1", str(isExistsKey))
isExistsItem = ('key2', 3) not in dict_sample.items()
log("CONTAINS key2:3", str(isExistsItem))
log_add_line(1)

# ＞dict#get
# 第１引数でキー、第２引数で存在しない場合の値を指定する
log(' - dict#get')
key1Value = dict_sample.get('key1', 10)
key4Value = dict_sample.get('key4', 10)
log('GET not default(key1)', key1Value)
log('GET default(key4)', key4Value)
log_add_line(1)

# ＞dict#setdefault
# キーが存在しない場合のみ追加を行う
log(' - dict#setdefault')
numStr = '123975849 223410 3274393'
count = {}
for char in numStr:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
log('SET DEFAULT(文字カウント)(pprint.pprint):')
# pprintを利用すると、内容をソートして表示することが可能
import pprint
pprint.pprint(count)
# 文字列として取得したい場合は、pprint#pformatで取得可能
log('同じ結果(pprint.pformat):')
log(pprint.pformat(count))
log_add_line()


# COPY（list, tuple, dict） +++++++++++++++++++++++
# copyモジュールのインポートが必要
log("＞COPY(list, tuple, dict) ---------------")
import copy
list_copy_target = ['A', 'B', 'C', 'D']
dict_copy_target = {'A': 1, 'B' : 2}
list_copy = copy.copy(list_copy_target)
dict_copy = copy.copy(dict_copy_target)
# 編集
list_copy[0] = 'COPY'
dict_copy['A'] = 'COPY'
log('ORIGINAL LIST', list_copy_target)
log('COPY LIST', list_copy)
log('ORIGINAL dict', dict_copy_target)
log('COPY dict', dict_copy)
log_add_line(1)

# ＞リスト/タプルのDEEP COPY
log("＞DEEP COPY(list, tuple, dict) ---------------")
list2d_deep_copy_target = [[1,2,3], ['A', 'B', 'C']]
list2d_copy = copy.copy(list2d_deep_copy_target)
list2d_deep_copy = copy.deepcopy(list2d_deep_copy_target)
# 編集
list2d_copy[1][0] = 'COPY'
list2d_deep_copy[1][0] = 'DEEP COPY'
log('ORIGINAL LIST', list2d_deep_copy_target)
log('COPY LIST', list2d_copy)
log('DEEPCOPY LIST', list2d_deep_copy)
log_add_line()
