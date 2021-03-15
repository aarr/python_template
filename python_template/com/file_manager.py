# file_manager.py
'''ファイル、ディレクトリ操作Utility
'''
import sys, os,shelve, shutil

# basic（パッケージ）、ext（モジュール）それぞれから呼び出されるため、直接パスを指定
# 呼び出され方によって、読む階層が変わるため
script_dir = os.path.abspath(__file__)
sys.path.append(os.path.dirname(script_dir))
from console import *

def makedir(path):
    ''' ディレクトリ作成
    '''
    try:
        os.makedirs(path)
    except FileExistsError as error:
        # 既にフォルダが存在する場合はそのまま処理をすすめる
        log('DO NOT MAKE DIR. ALREADY EXISTS : {0}'.format(path))
    else:
        log('COMPLETE MAKE DIR : {0}'.format(path))

def remove(path):
    '''ファイル/ディレクトリ一括削除
    '''
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
            # 下記でも同等の挙動
            #os.unlink(path)
    except FileNotFoundError as error:
        log('NOT EXISTS : {0}'.format(path))
    else:
        log('COMPLETE REMOVE : {0}'.format(path))

def read_file(file_path, isDebug=True):
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

def readline_file(file_path, isDebug=True):
    '''ファイル１行毎読込
    '''
    log('READ', file_path)
    # withでopenすることでclose漏れがなくなる
    with open(file_path) as file:
        line = file.readline()
        lineCount = 0
        while line:
            lineCount = lineCount + 1
            if isDebug:
                log('LINE({0})'.format(str(lineCount)), remove_line_separator(line))
            line = file.readline()

def readlines_file(file_path, isDebug=True):
    '''ファイル全行読込
    '''
    with open(file_path) as file:
        lines = file.readlines()
        if isDebug:
            log('READ LINES', lines)
    
def write_file(file_path, mode, contennt=''):
    ''' ファイル書込
    '''
    with open(file_path, mode) as file:
        writeNum = file.write(contennt)
        log('WRITE FILE', 'Write Character', writeNum)
        # 書き込んだ内容表示
        readline_file(file_path)

def make_file(file_path, mode='w'):
    '''ファイル作成
    '''
    file = None
    try:
        file = open(file_path, mode)
    except Exception as ex:
        log('ERROR', ex)
    return file;

def save_shelve(key, value, file_path='temp_data'):
    shelve_file = shelve.open(file_path)
    shelve_file[key] = value
    shelve_file.close()
    log('save shelve')

def get_shelve(key, file_path='temp_data'):
    shelve_file = shelve.open(file_path)
    value = shelve_file[key]
    shelve_file.close()
    log('get shelve')
    return value

def remove_line_separator(line):
    _line = str(line)
    # 3項演算子
    return _line.strip('\n').strip('\r') if line != None else line;

def seek(file_path, point, chunk=0): 
    """読み込みポイントを指定可能
    Aargs
        file_path(str): 読み込みファイル
        point(int): 読み込み開始ポイント
        chunk(int): 読み込み量
    """
    with open(file_path, 'r') as file:
        file.seek(point)
        log('POINT:{}, CHUNK:{}'.format(point, chunk if chunk != 0 else 'ALL'), file.read(chunk) if chunk != 0 else file.read())

