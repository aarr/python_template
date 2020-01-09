#============================
# 関数
#============================
import random
print("＞関数---------------")
# 最もシンプルな関数書き方
def func() :
    print("called func")
    # returnを記載しない場合、returnだけ記載して返却値を記載しない場合、Noneが返却される

# 引数、戻り値ありの関数
def funcArgs(arg1, arg2) :
    arg1Message = "引数１：" + str(arg1)
    arg2Message = "引数２：" + str(arg2)
    print(arg1Message)
    print(arg2Message)
    return arg1Message + "、" + arg2Message

# スコープ確認関数
# 一度ローカルスコープで利用した変数を、グローバル変数として利用することはできない
def confirmLocalGlobal(funcArg) :
    arg = "local"
    print("Scope確認（arg）：" + arg)
    print("Scope確認（funcArg）：" + funcArg)
    global globalArg
    print("明示的グローバル変数表示（globalArg）" + str(globalArg))
    globalArg = globalArg + " Changed"
    print("明示的グローバル変数変更（globalArg）" + globalArg)

res = func() # Noneが返却される
print("結果はNone？：" + str(res == None))
print("戻り値：" + funcArgs("AAAA", random.randint(1, 9)))


# キーワード変数
print("＞関数（キーワード変数）---------------")
# printにはsepとendというキーワード変数が定義されている。
print("Hello", "World")
print("Hello", "World", sep=",")
print("Hello", "World", sep=",", end="END\r\n")


# スコープ
# 考え方は他のスクリプト言語と同様
# スコープが異なれば、同じ変数名を利用することは許容されている
print("＞スコープ ---------------")
arg = "Global"
funcArg = "Global"
globalArg = "Global"
confirmLocalGlobal("local")  # グローバル変数更新を含む
print("グローバル変更確認（globalArg）：" + globalArg)
