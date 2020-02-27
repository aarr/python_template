#!/usr/bin/env python3
# file.py

""" ファイル
ファイル管理サンプル集
"""

from console import *
import file_operation, send2trash

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
file_operation.writeFile(copy_test_file, 'w')
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
file_operation.writeFile(move_test_file, 'w')
file_operation.makedir(move_test_path)
shutil.move(move_test_file, move_test_path)
log('MOVE', '{0} -> {1}'.format(move_test_file, move_test_path))
log_add_line(1)

# ゴミ箱移動`
log(' - send to trash')
trash_test_file = os.path.join(work_dir, 'trash_test_file')
file_operation.writeFile(trash_test_file, 'a', 'trash data')
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
