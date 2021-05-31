#!/usr/bin/env python3
"""マルチスレッド"""
import datetime
import time
import threading

import com.console

log = com.console.log
log_add_line = com.console.log_add_line

log('#============================')
log('# Multi Thread')
log('#============================')
log('MultiThread start')


def func(thread_name, running_time, interval=1):
    """MultiTreadテスト用関数
    Sleepしてログ出力するのみ

    Args:
        thread_name (str): スレッド名
        running_time (int): 実行時間
        interval (int, optional): インターバル. Defaults to 1.
    """
    log('NAME:{0} start'.format(thread_name))

    now = datetime.datetime.now()
    break_span = datetime.timedelta(seconds=running_time)
    break_time = now + break_span
    while datetime.datetime.now() < break_time:
        time.sleep(interval)
        log('{0} running...'.format(thread_name))

    log('NAME:{0} end'.format(thread_name))
    log_add_line(1)


log('Thread機動')
log(' EX) threading.Threa(target=func, args=[], kwargs={})')
log(' - 実行対象 : targetに関数名を指定')
log(' - 引数 : argsに配列で指定')
log(' - キーワード変数 : kwargsにdict型で指定')
log_add_line(1)
log('Thread完了待ち')
log(' - Thread.join()でThreadの完了を待つことが可能')
log_add_line()


log('thread running start')
# Thread1開始
thread1 = threading.Thread(target=func, args=['Thread1', 3])
log('Thread1 up')
thread1.start()
# Thread2開始
thread2 = threading.Thread(target=func, args=['Thread2', 5], kwargs={'interval' : 2})
log('Thread2 up')
thread2.start()
log('thread running complete')
log_add_line(1)

# スレッド終了待ち
thread1.join()
log('threa1 join')
log_add_line(1)

thread2.join()
log('threa2 join')
log_add_line(1)

log('MultiThread end')
