#!/usr/bin/env python3
# function.py
#
""" 関数
関数サンプル集
"""

from com.console import *

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

    log(" -ローカル変数確認 ---------------")
    log("locals", locals())


# 考え方は他のスクリプト言語と同様
# スコープが異なれば、同じ変数名を利用することは許容されている
arg = "Global"
func_arg = "Global"
global_arg = "Global"
confirm_local_global("local")  # グローバル変数更新を含む
log("CONFIRM GLOBAL ARG(global_arg)", global_arg)
log_add_line(1)

log(" -グローバル変数確認 ---------------")
log("globals", globals())
log_add_line(1)


# デコレータ
log("＞デコレータ ---------------")
def decorator_func(func):
    def wrapper(*args, **kwargs):
        log('Start')
        result = func(*args, **kwargs)
        log('End')
        return result
    return wrapper

def decorator_more(func):
    def wrapper(*args, **kwargs):
        log('FUNC:', func.__name__)
        log('ARGS:', args)
        log('KWARGS:', kwargs)
        result = func(*args, *kwargs)
        log('RESULT:', result)
        return result
    return wrapper

def add_num(a, b):
    log('ADD')
    return a + b

# デコレータファンクションはアノテーションで指定することが可能
# 複数指定することが可能であり、指定した順にデコレータが実行される
@decorator_func
@decorator_more
def minus_num(a, b):
    log('MINUS')
    return a - b

# 実行
dec_add_func = decorator_func(add_num)
log('DECORATOR', dec_add_func(10, 20))
# 実行
log_add_line(1)
log('DECORATOR WITH ANNOTATION', minus_num(10, 20))
log_add_line()


# lambda
log("＞lambda ---------------")
week = {'Mon', 'Tue', 'wed', 'thu', 'Fri', 'Sta', 'sun'}
def cheange_words(words, func):
    for word in words:
        log(func(word))

log('Original Week Data', week)
log('labmda呼び出し:capitalizse')
cheange_words(week, lambda word: word.capitalize())
log('labmda呼び出し:lower')
cheange_words(week, lambda word: word.lower())
log_add_line(1)

# Generator
log("＞Generator(yield) ---------------")
import time
# yieldにより、Generatorであると判断される
# 一度にすべての計算を行うのではなく、yieldごとに処理を分割して実施できる
def generator():
    # １回目の呼び出しで返却される
    yield 10
    # ２回目の呼び出しが行われた際に処理される
    log('SLEEP:1sec')
    time.sleep(1)
    yield 20
    # ３回目の呼び出しが行われた際に処理される
    log('SLEEP:2sec')
    time.sleep(2)
    yield 30

g = generator()
log('GENERATOR CALL', 1)
log('1回目', next(g))
log('GENERATOR CALL', 2)
log('2回目', next(g))
log('GENERATOR CALL', 3)
log('3回目', next(g))
log_add_line(1)

log("＞Generator内包表記 ---------------")
# ()で記載するが、tuppleではなくGeneratorとして認識される
g = (i for i in range(10) if i % 2 == 0)
log('TYPE', type(g))
for val in g:
    log('VALUE', val)
log_add_line()