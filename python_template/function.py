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
def func_args(arg1, arg2) :
    arg1Message = "引数１：" + str(arg1)
    arg2Message = "引数２：" + str(arg2)
    print(arg1Message)
    print(arg2Message)
    return arg1Message + "、" + arg2Message

res = func() # Noneが返却される
print("結果はNone？：" + str(res == None))
print("戻り値：" + func_args("AAAA", random.randint(1, 9)))

# キーワード変数
print("＞関数（キーワード変数）---------------")
# printにはsepとendというキーワード変数が定義されている。
print("Hello", "World")
print("Hello", "World", sep=",")
print("Hello", "World", sep=",", end="END\r\n")


# スコープ
print("＞スコープ ---------------")
# スコープ確認関数
# 一度ローカルスコープで利用した変数を、グローバル変数として利用することはできない
def confirm_local_global(func_arg) :
    arg = "local"
    print("Scope確認（arg）：" + arg)
    print("Scope確認（func_arg）：" + func_arg)
    global global_arg
    print("明示的グローバル変数表示（global_arg）" + str(global_arg))
    global_arg = global_arg + " Changed"
    print("明示的グローバル変数変更（global_arg）" + global_arg)

# 考え方は他のスクリプト言語と同様
# スコープが異なれば、同じ変数名を利用することは許容されている
arg = "Global"
func_arg = "Global"
global_arg = "Global"
confirm_local_global("local")  # グローバル変数更新を含む
print("グローバル変更確認（global_arg）：" + global_arg)


# 例外処理
print("＞例外処理 ---------------")
# 割り算（サンプル関数）
def divide(arg1, arg2) :
    try:
        result =  arg1 / arg2 
    # except 例外 as 変数名: とし、発生した例外を利用することが可能
    # exceptを続けていくことで、複数のエラーハンドリングが可能
    except ZeroDivisionError as error:
        print("ERROR : ", end="")
        print(error)
    # Exceptionを明示的に定義しないと、全ての例外を補足する。
    except:
        print("エラー発生！")
    # 例外が発生しなかった場合の処理を記述可能
    else:
    # 必ず実行する
        return result
    finally:
        print("Finally")

print("10 / 3 = " + str(divide(10, 3)))
print("10 / 0 = " + str(divide(10, 0)))   # エアーメッセージが表示され、戻り値としてはNoneとなる
