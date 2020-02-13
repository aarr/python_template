#!/usr/bin/env python3
# file.py

""" ファイル
ファイル操作サンプル集
"""

from console import *

log('#============================')
log('# ファイル操作')
log('#============================')

# 基本 +++++++++++++++++++++++
# フォルダの区切りはOS毎に異なる。両方に対応するよう実装するには、os.path.joinを利用することで実現可能
# Windows : \
# Linux, Mac : /
import os
log('> osパッケージ基本')
log(' - ディレクトリ表示、ディレクトリ移動')
log('PATH', os.path.join('usr', 'bin', 'span'))
log('CURRENT DIR', os.getcwd())
# ユーザのホームディレクトリ
home_dir = os.path.expanduser('~')
log('HOME DIR', home_dir)
log_add_line(1)
# 場所移動
dir_script = os.path.abspath(__file__)
os.chdir(home_dir)
log('CHANGE DIRECTORY -> ' + home_dir) 
log('CURRENT DIR', os.getcwd())

# ディレクトリ作成
# 中間ディレクトリも作成される
# os.mkdirも新規ディレクトリ作成可能だが、既存ディレクトリに対しての追加しかできない。
# 中間ディレクトリ毎一括で作成するにはos.makedirsを使うのがよい
log(' - ディレクトリ作成')
work_dir = home_dir + '/python_work'
worK_dir_test_makedir = work_dir + '/makedirs_test'
try:
    os.makedirs(worK_dir_test_makedir)
except FileExistsError as error:
    # 既にフォルダが存在する場合はそのまま処理をすすめる
    log('DO NOT MAKE DIR. ALREADY EXISTS')
else:
    log('COMPLETE MAKE DIR',)
log('WORK DIR', worK_dir_test_makedir)
os.chdir(worK_dir_test_makedir)
log_add_line(1)

log(' - パス判定')
log('GET ABSOLUTE PATH', os.path.abspath('.'))
log('IS ABSOLUTE PATH(.)', os.path.isabs('.'))
log('IS ABSOLUTE PATH(/)', os.path.isabs('/'))
# 第２引数（home_dir）から、第１引数（ルードディレクトリ）への相対パスを表現`
log('GET RELATIVE PATH', os.path.relpath('/', home_dir)) 
log_add_line(1)

log(' - その他')
log('GET BASENAME', os.path.basename(worK_dir_test_makedir))
# 指定した末尾のディレクトリ、ファイル名を取得
log('GET DIRNAME', os.path.dirname(worK_dir_test_makedir))
# basenameまでのパスと分けて取得したい場合はsplitで取得可能（タプル）
log('SPLIT', os.path.split(worK_dir_test_makedir))
# ファイル/ディレクトリサイズ確認（byte）
log('SIZE', os.path.getsize(worK_dir_test_makedir), 'byte')
# 指定したパス以下のディレクトリ、ファイルの一覧を取得可能
log('LIST DIR/FILE', os.listdir(home_dir))
# ファイルパス存在確認
log('EXISTS PATH', os.path.exists(worK_dir_test_makedir))
# ファイル確認
log('IS FILE', os.path.isfile(worK_dir_test_makedir))
# ディレクトリ確認
log('IS DIR', os.path.isdir(worK_dir_test_makedir))
log_add_line()


# ファイル読込／書込 +++++++++++++++++++++++
log('>ファイル読込／書き込み')
file_path_read_test = work_dir + '/file_test/TEST_READ.txt'
file_path_write_test = work_dir + '/file_test/TEST_WRITE.txt'

def readFile(file_path) :
    '''ファイル読込
    '''
    # openでFileオブジェクト取得
    # readで内容読込
    # closeでファイルを閉じる
    file = None
    try:
        # r指定で読み取り専用として開く
        file = open(file_path, 'r')
        content = file.read()
        log('READ', file_path, content)
    except Exception as ex:
        log('ERROR', ex)
    finally:
        if file != None:
            file.close()

def readlineFile(file_path):
    '''ファイル１行毎読込
    '''
    file = None
    try:
        file = open(file_path)
        line = file.readline()
        log('READ LINE START')
        while line:
            log(remove_line_separator(line))
            line = file.readline()
        log('READ LINE END')
    except Exception as ex:
        log('ERROR', ex)
    finally:
        if file != None:
            file.close()

def readlinesFile(file_path):
    '''ファイル全行読込
    '''
    file = None
    try:
        file = open(file_path)
        lines = file.readlines()
        log('READ LINES', (lines))
    except Exception as ex:
        log('ERROR', ex)
    finally:
        if file != None:
            file.close()

def writeFile(file_path, mode, contennt):
    ''' ファイル書込
    '''
    file = None
    try:
        file = open(file_path, mode)
        writeNum = file.write(contennt)
        log('WRITE FILE', 'Write Character', writeNum)
    except Exception as ex:
        log('ERROR', ex)
    finally:
        if file != None:
            file.close()
            # 書き込んだ内容表示
            readlineFile(file_path)

def saveShelve(key, value):
    shelve_file = shelve.open('temp_data')
    shelve_file[key] = value
    shelve_file.close()
    log('save shelve')

def getShelve(key):
    shelve_file = shelve.open('temp_data')
    value = shelve_file[key]
    shelve_file.close()
    log('get shelve')
    return value

def remove_line_separator(line):
    _line = str(line)
    # 3項演算子
    return _line.strip('\n').strip('\r') if line != None else line;

# ファイル読込
log(' - read')
readFile(file_path_read_test)
log(' - readline')
readlineFile(file_path_read_test)
log(' - readlines')
readlinesFile(file_path_read_test)
log_add_line(1)

# ファイル書込
# w：書込（新規）
# a：書込（追記）
log(' - write(w)')
writeFile(file_path_write_test, 'w', 'write file w mode\nnew line\n')
log_add_line(1)
log(' - write(a)')
writeFile(file_path_write_test, 'a', 'write file a mode\nadd line\nadd line\n')
log_add_line(1)


# shelve（シェルフ：棚） +++++++++++++++++++++++
# バイナリファイルとして一時的に保存が可能
log(' - shelve')
import shelve
saveShelve('condition', {'key1' : 1, 'key2' : 10})
condition = getShelve('condition')
log('SHELVE', condition)
log_add_line()


# pprint.pformat +++++++++++++++++++++++
# Pythonでそのまま利用できる形でファイル保存が可能
log(' - pprint.pformat -> file')
import pprint
sample_data = [{'key1' : 'value1'}, {'key2' : 'value2', 'key3' : 'value3'}]
# 後にimportするため、change directoryする前のスクリプト実行ディレクトリに配置する
content_formated = 'sample_data_formatted = ' + pprint.pformat(sample_data) + ';\n'
log('PPRINT.PFORMAT', content_formated)
# このファイルを後ほどimportする
filepath_format_test = os.path.dirname(dir_script) + '/pprintTest.py'
writeFile(filepath_format_test, 'w', content_formated)
log('import pprint.pformat file')
import pprintTest
sample_data_formatted = pprintTest.sample_data_formatted
log('AFTER IMPORT(ALL)', sample_data_formatted, title_space=20)
log('AFTER IMPORT(0)', sample_data_formatted[0], title_space=20)
log('AFTER IMPORT(0)', sample_data_formatted[1], title_space=20)
log_add_line()


