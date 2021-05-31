#!/usr/bin/env python3
# shell.py
""" subprocessを利用して、シェルの実行を行うサンプル
"""

import subprocess

import com.console

log = com.console.log
log_add_line = com.console.log_add_line


# =========================================================
# シェルコマンド実行
log('EXECUTE SHELL(Patter1)', 'ls -al')
subprocess.run(['ls', '-al'])
log_add_line(1)


# =========================================================
# 非推奨。ShellInjectionができてしまうのでセキュリティ的によろしくない
# エラーになっても後続処理へ流れるので
log('EXECUTE SHELL(Patter2)', 'ls -al')
subprocess.run('ls -la', shell=True)
log_add_line(1)


# =========================================================
log('EXECUTE SHELL(Error)', 'lsxxx -al')
result = subprocess.run('lsxxx -la', shell=True)
# returnCodeで後続処理のハンドリングを行う
log('RETURN CODE', result.returncode)
# もしくはcheck=Trueとして、エラーを発生させる
try:
    subprocess.run('lsxxx -la', shell=True, check=True)
except Exception as e:
    log('EXCEPT ERROR', e)
log_add_line(1)


# =========================================================
# ShellInjectionを回避しつつ、パイプを利用する場合
log('EXECUTE SHELL(Pattern3)', 'PIPE利用')
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'python'],
                      stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
result = p2.communicate()[0]
log('RESULT', result)
