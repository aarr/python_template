#!/usr/bin/env python3
# file_control.py

""" ファイル
ファイル・ディレクトリの作成は情報取得
"""

from com.console import *
import basic.file_operation as file_operation, send2trash
import com.file_manager as fm

log('#============================')
log('# ファイル管理')
log('#============================')
import shutil ,os

home_dir = os.path.expanduser('~')
base_work_dir = os.path.join(home_dir, 'work_python')
work_dir = os.path.join(base_work_dir, 'file_control')
# 一度workディレクトリを削除
file_operation.remove(work_dir)

# ファイルコピー
log(' - copy')
copy_test_file = os.path.join(work_dir, 'copy_target.txt')
copied_file = os.path.join(work_dir, 'copied.txt')
file_operation.makedir(work_dir)
file_operation.write_file(copy_test_file, 'w')
shutil.copy(copy_test_file, copied_file)
log_add_line(1)

# ファイル名変更
log(' - rename')
rename_test_file = os.path.join(work_dir, 'copy_test-renamed.txt')
log('MOVE', '{0} -> {1}'.format(copy_test_file, rename_test_file))
shutil.move(copy_test_file, rename_test_file)
log_add_line(1)

# ファイル移動
log(' - move')
move_test_path = os.path.join(work_dir, 'move_test')
move_test_file = os.path.join(work_dir, 'move.txt')
file_operation.write_file(move_test_file, 'w')
file_operation.makedir(move_test_path)
shutil.move(move_test_file, move_test_path)
log('MOVE', '{0} -> {1}'.format(move_test_file, move_test_path))
log_add_line(1)

# ゴミ箱移動
log(' - send to trash')
trash_test_file = os.path.join(work_dir, 'trash_test_file')
file_operation.write_file(trash_test_file, 'a', 'trash data')
send2trash.send2trash(trash_test_file)
log('SEND2TRASH', trash_test_file)
log_add_line(1)

# ディレクトリツリー渡り歩き
log(' - walk')
for foldername, subfolders, filenames in os.walk(base_work_dir):
    log('CURRENT DIR', foldername)
    for subfolder in subfolders:
        log('SUB DIR', subfolder)
    for filename in filenames:
        log('FILE', filename)
    log_add_line(1)


# =========================================================
# ファイル操作ライブラリ
# ファイル作成、作成したディレクトリ内の情報確認
import pathlib
import glob

log(' - pathlib:touch')
# 空ファイルが簡単に作成できる。Python3から導入。それ以前はファイルのOpenなどしなければ行けなかった。
pathlib_test_dir = os.path.join(work_dir, 'filelib')
os.mkdir(pathlib_test_dir)
pathlib.Path(work_dir + '/filelib/empty.txt').touch()
# globで指定ディレクリの状態を確認可能
# os.listdirとはファイル名だけか、パスまでつくか
log('OS#LISTDIR:', os.listdir(pathlib_test_dir))
log('GLOB:', glob.glob(pathlib_test_dir + '/*'))
# 作成したファイルをすべて削除
shutil.rmtree(pathlib_test_dir)
log('GLOB(SHUTIL#RMTREE):', glob.glob(pathlib_test_dir + '/*'))
log_add_line(1)


# =========================================================
# tarファイル作成／解凍
import tarfile

compress_test_dir = os.path.join(work_dir, 'compressTest')
os.mkdir(compress_test_dir)
compress_test_file_path = os.path.join(compress_test_dir, 'content1.txt')
# ファイル作成、COPY
pathlib.Path(compress_test_file_path).touch()
shutil.copy(os.path.join(compress_test_dir, 'content1.txt')
            ,os.path.join(compress_test_dir, 'content2.txt'))
log('TAR TARGET', glob.glob(os.path.join(compress_test_dir, '*')))
fm.write_file(compress_test_file_path, 'w', 'Tar Compress Test')

# tar作成
# https://docs.python.org/ja/3/library/tarfile.html
log(' - compress tar')
current_dir = os.getcwd()
tar_path = os.path.join(compress_test_dir, 'test.tar.gz')
with tarfile.open(tar_path, 'w:gz') as tr:
    os.chdir(work_dir)
    # tarに含まれる階層は、指定した階層が含まれる。ルートから指定すればその階層が含まれる
    tr.add('compressTest')
    # tr.add(compress_test_dir)
    log('TAR FILE', glob.glob(os.path.join(compress_test_dir, '*')))

# tar解凍
log(' - extract tar')
with tarfile.open(tar_path, 'r:gz') as tr:
    # すべて展開
    tr.extractall(path=os.path.join(compress_test_dir, 'extract_tar'))
    log('TAR EXTRACT ALL', glob.glob(os.path.join(compress_test_dir, '*')))
    # 展開せずに指定ファイルの内容を確認
    # tarファイル内の階層を見る
    with tr.extractfile(os.path.join('compressTest', 'content1.txt')) as f:
        log('TAR EXTRACT FILE', f.read())
log_add_line(1)


# =========================================================
# zipファイル作成／解凍
import zipfile

# zip作成
log(' - compress zip')
zip_path = os.path.join(compress_test_dir, 'test.zip')
fm.write_file(compress_test_file_path, 'w', 'Zip Compress Test')
with zipfile.ZipFile(zip_path, 'w') as zf:
    # compress_test_dir内のファイルをすべてzipに含める
    for f in glob.glob(os.path.join('.', '**'), recursive=True):
        zf.write(f)
    log('ZIP FILE', glob.glob(os.path.join(compress_test_dir, '*')))

# zip解凍
log(' - extract zip')
with zipfile.ZipFile(zip_path, 'r') as zf:
    # すべて展開
    zf.extractall(path=os.path.join(compress_test_dir, 'extract_zip'))
    log('ZIP EXTRACT ALL', glob.glob(os.path.join(compress_test_dir, '*')))
    # 展開せずに指定ファイルの内容を確認
    with zf.open(os.path.join('compressTest', 'content1.txt')) as f:
        log('ZIP EXTRACT FILE', f.read())
log_add_line(1)


# =========================================================
# tempファイル
import tempfile

# 使い終わったら削除してくれる
#　作業用のファイルとして利用が可能
log(' - make tempfile')
with tempfile.TemporaryFile(mode='w+') as tf:
    tf.write('temp content')
    tf.seek(0)
    log('TEMP FILE CONTENT', tf.read())
    
# ファイルを残すことも可能
log(' - make tempfile(not delete)')
with tempfile.NamedTemporaryFile(delete=False) as tf:
    temp_file_path = tf.name
    log('TEMP FILE PATH', temp_file_path)
    with open(tf.name, 'w+') as f:
        f.write('not delete file')
        f.seek(0)
        log('TEMP FILE CONTENT', tf.read())
# ファイルが消されておらず、残っていることが確認できる
log('TEMP FILE EXISTS', os.path.exists(temp_file_path))

# tempDirectory作成 
# 使い終わったら削除される
log(' - make tempDirectory')
with tempfile.TemporaryDirectory() as td:
    log('TEMP DIRECTORY', td)
log('TEMP DIRECTORY EXISTS', os.path.exists(td))
log_add_line(2)
