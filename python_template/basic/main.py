# main.py

""" Pythonサンプル
Python基本実装集
引数にskipとつける事で、その他スクリプトの実行をスキップする
"""
from com.console import *

def execute():
    """Excample function with types documentted in the docstring.
    関数の説明を記述。execute.__doc__によって参照可能

    Args:
        param1 (int): The first paramter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwire
    """
    import itertools, random, traceback
    import sys, datetime, time

    log('+++++++++++++++++++ START +++++++++++++++++++')
    log('#============================')
    log('# 基本')
    log('#============================')
    skip_other_script = True if len(sys.argv) == 2 and sys.argv[1] == 'skip' else False
    log('SKIP OTHER SCRIPT', skip_other_script)

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
    log('TYPE(int)', int == type(100))
    log('TYPE(list)', list == type([1, 2, 3]))
    log('TYPE(dist)', dict == type({'a' : 'b', '1' : '2'}))
    log('TYPE(set)', set == type({1 ,2 ,3}))
    log('TYPE(tuple)', tuple == type((1 ,2 ,3)))

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
    log(' -日時')
    # 現在時刻の取得
    now = datetime.datetime.now()
    formatted_now = now.strftime('%Y%m%d_%H%M%S')
    log('NOW', formatted_now)
    log('NOW FORMAT', '{0}年{1}月{2}日 {3}時{4}分{5}秒'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))
    # datetime.datetime.now()と同じ
    now2 = datetime.datetime.fromtimestamp(time.time())
    log('NOW2', now2.strftime('%Y%m%d_%H%M%S'))
    log_add_line(1)
    # タイムスタンプからの変換
    dt = datetime.datetime.fromtimestamp(1000 * 1000 * 1000)
    log('EPOC FROM 1000 * 1000 * 1000sec', dt)
    log_add_line(1)
    # 指:日時
    any_dt = datetime.datetime(2020, 4, 1, 12, 59, 10)
    log('ANY DATETIME', any_dt.strftime('%Y%m%d_%H%M%S'))
    log('TO STRING FORMAT')
    log(now.strftime('%Y'), '%Y：4桁西暦')
    log(now.strftime('%y'), '%y：西暦下2桁')
    log(now.strftime('%m'), '%m：月')
    log(now.strftime('%B'), '%B：月名')
    log(now.strftime('%b'), '%b：月略名')
    log(now.strftime('%j'), '%j：年初からの日数')
    log(now.strftime('%w'), '%w：曜日')
    log(now.strftime('%A'), '%A：曜日名')
    log(now.strftime('%a'), '%a：曜日略名')
    log(now.strftime('%H'), '%H：時(24時間制)')
    log(now.strftime('%M'), '%M：分')
    log(now.strftime('%S'), '%S：秒')
    log(now.strftime('%p'), '%p：AM/PM')
    log(now.strftime('%%'), '%%：%文字(ESCAPE)')
    log_add_line(1)

    # 期間 
    log(' -期間')
    break_span = datetime.timedelta(seconds=3)
    break_time = now + break_span
    log('BREAK SECONDS', break_span)
    # 指定時間まで停止
    log('BREAK START', datetime.datetime.now())
    while datetime.datetime.now() < break_time:
        time.sleep(1)
        log('BREAK...')
    log('BREAK END', datetime.datetime.now())

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
    log_add_line(1)
    for i in range(10, 13) :
        log("FOR COUNT", i)
    log_add_line(1)
    for i in range(100, 130, 10) :
        log("FOR COUNT", i)
    log_add_line(1)

    # indexも必要な場合には、enumerateを利用する
    for index, val in enumerate(range(100, 130, 10)):
        log("FOR COUNT {0}".format(index), val)
    log_add_line(1)

    # 逆順でループしたい場合には、reversedを利用する
    for index, val in enumerate(reversed(range(100, 130, 10))):
        log("FOR(REVERSED) {0}".format(index), val)
    log_add_line(1)

    # 複数配列を一度にループしたい場合
    for val1, val2 in zip((1, 2, 3), (10, 20, 30)):
        log("FOR(ZIP)", 'VALUE1 : {0}, VALUE2 : {1}'.format(val1, val2))
    log_add_line(1)

    # ネストループを１階層で記述したい場合
    for val, nest_val in itertools.product(range(3), range(10, 40, 10)):
        log("FOR(PRODUCT)", 'VALUE : {0}, NEST_VALUE2 : {1}'.format(val, nest_val))
    log_add_line(1)



    # dictを利用したfor文
    # iteratorを３種類選択可能。keys,values,items
    dict_for_sample = {'hoge' : '10', 'fuga' : '20', 'fage' : '30'}
    for key  in dict_for_sample.keys() :
        log('DICT CONTENT', 'KEY:' + key + ', VALUE:' + dict_for_sample[key])
    log_add_line()


    # import +++++++++++++++++++++++
    # import moduleName1, moduleName2, moduleName
    log("＞import---------------")
    log("RANDOM", random.randint(1, 10))
    log_add_line(1)

    # from moduleName import functionName(*指定可能)
    # moduleNameを省略して呼び出すことが可能。module名が記載されている方がわかりやすいのでimport飲みの方がよい
    log("＞from import---------------")
    from random import randint
    log("RANDOM", randint(1, 10))
    log_add_line()

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


    if skip_other_script == False:
        # コンテナ型  +++++++++++++++++++++++
        import basic.container

        # 関数  +++++++++++++++++++++++
        import basic.function 

        # 文字列操作  +++++++++++++++++++++++
        import basic.str_operation

        # 正規表現  +++++++++++++++++++++++
        import basic.regex

        # ファイル操作  +++++++++++++++++++++++
        import basic.file_operation 
        basic.file_operation.main()

        import basic.file_control

        # with句  +++++++++++++++++++++++
        import basic.with_sample


    # プログラム終了 +++++++++++++++++++++++
    log('+++++++++++++++++++ END +++++++++++++++++++')
    import sys
    sys.exit()
    log("ここにはたどり着かない")

