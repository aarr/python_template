#============================
# 関数
#============================
from console import *
log('#============================')
log('# 関数')
log('#============================')
import random
log("＞関数---------------")
# 最もシンプルな関数書き方
def func() :
    log("called func")
    # returnを記載しない場合、returnだけ記載して返却値を記載しない場合、Noneが返却される

# 引数、戻り値ありの関数
def func_args(arg1, arg2) :
    arg1Message = "ARG1:" + str(arg1)
    arg2Message = "ARG2:" + str(arg2)
    log(arg1Message)
    log(arg2Message)
    return arg1Message + ", " + arg2Message

res = func() # Noneが返却される
log("IS RESULT NONE", res == None)
log("RESULT", func_args("AAAA", random.randint(1, 9)))
indent()


# キーワード変数
log("＞関数（キーワード変数）---------------")
# logにはsepとendというキーワード変数が定義されている。
log('OPTIONAL ARG', "Hello", "World")
log('OPTIONAL ARG', "Hello", "World", sep=",")
log('OPTIONAL ARG', "Hello", "World", sep=",", end="END\r\n")
indent(1)

# スコープ
log("＞スコープ ---------------")
# スコープ確認関数
# 一度ローカルスコープで利用した変数を、グローバル変数として利用することはできない
def confirm_local_global(func_arg) :
    arg = "local"
    log("SCOPE(arg)", arg)
    log("SCOPE(func_arg)", func_arg, title_space=50)
    global global_arg
    log("EXPLICIT GLOBAL ARG(global_arg)", global_arg, title_space=50)
    global_arg = global_arg + " Changed"
    log("EXPLICIT GLOBAL ARG EDITED(global_arg)", global_arg, title_space=50)

# 考え方は他のスクリプト言語と同様
# スコープが異なれば、同じ変数名を利用することは許容されている
arg = "Global"
func_arg = "Global"
global_arg = "Global"
confirm_local_global("local")  # グローバル変数更新を含む
log("CONFIRM GLOBAL ARG(global_arg)", global_arg)
indent()

# 例外処理
log("＞例外処理 ---------------")
# 割り算（サンプル関数）
def divide(arg1, arg2) :
    result = None
    try:
        result =  arg1 / arg2 
    # except 例外 as 変数名: とし、発生した例外を利用することが可能
    # exceptを続けていくことで、複数のエラーハンドリングが可能
    except ZeroDivisionError as error:
        log("ERROR(ZeroDivision)", error)
    # Exceptionを明示的に定義しないと、全ての例外を補足する。
    except:
        log("ERROR", error)
    # 例外が発生しなかった場合の処理を記述可能
    else:
    # 必ず実行する
        return result
    finally:
        log("FINALLY RESULT", result)

log("10 / 3 = ", divide(10, 3))
indent(1)
log("10 / 0 = ", divide(10, 0))   # エアーメッセージが表示され、戻り値としてはNoneとなる
indent()