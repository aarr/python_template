#!/usr/bin/env python3
# function.py
#
""" 関数
関数サンプル集
"""

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
log_add_line()


# キーワード変数
log("＞関数（キーワード変数）---------------")
# logにはsepとendというキーワード変数が定義されている。
log('OPTIONAL ARG', "Hello", "World")
log('OPTIONAL ARG', "Hello", "World", sep=",")
log('OPTIONAL ARG', "Hello", "World", sep=",", end="END\r\n")
log_add_line(1)

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
log_add_line()