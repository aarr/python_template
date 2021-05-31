#!/usr/bin/env python3
""" ファイル
ファイル操作サンプル集
"""

import os
import pprint

import basic.pprint_test_data as pprint_test_data
import com.console
import com.file_manager as fm

log = com.console.log
log_add_line = com.console.log_add_line


def main():
    log('#============================')
    log('# ファイル操作')
    log('#============================')
    # 基本 +++++++++++++++++++++++
    # フォルダの区切りはOS毎に異なる。両方に対応するよう実装するには、os.path.joinを利用することで実現可能
    # Windows : \
    # Linux, Mac : /
    log('> osパッケージ基本')
    log(' - ディレクトリ表示、ディレクトリ移動')
    log('PATH', os.path.join('usr', 'bin', 'span'))
    log('CURRENT DIR', os.getcwd())
    # ユーザのホームディレクトリ
    home_dir = os.path.expanduser('~')
    log('HOME DIR', home_dir)
    log_add_line(1)
    # 場所移動
    current_dir = os.getcwd()
    dir_script = os.path.abspath(__file__)
    os.chdir(home_dir)
    log('CHANGE DIRECTORY -> ' + home_dir)
    log('CURRENT DIR', os.getcwd())

    # ディレクトリを移動するとimportする際のサーチパスが変わってしまう。
    # そのため、本に戻す
    os.chdir(current_dir)

    # ディレクトリ作成
    # 中間ディレクトリも作成される
    # os.mkdirも新規ディレクトリ作成可能だが、既存ディレクトリに対しての追加しかできない。
    # 中間ディレクトリ毎一括で作成するにはos.makedirsを使うのがよい
    log(' - ディレクトリ作成')
    work_dir = os.path.join(home_dir, 'work_python')
    # 一度ワークディレクトリ削除
    fm.remove(work_dir)
    worK_dir_test_makedir = os.path.join(work_dir, 'makedirs_test')
    fm.makedir(worK_dir_test_makedir)
    log('WORK DIR', worK_dir_test_makedir)
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
    file_path_test_dir = os.path.join(work_dir, 'file_test')
    fm.makedir(file_path_test_dir)
    file_path_test = os.path.join(file_path_test_dir, 'TEST.txt')

    # ファイル書込
    # w：書込（新規）
    # a：書込（追記）
    log(' - write(w)')
    fm.write_file(file_path_test, 'w', 'write file w mode\nnew line\n')
    log_add_line(1)
    log(' - write(a)')
    fm.write_file(file_path_test, 'a',
                  'write file a mode\nadd line\nadd line\n')
    log_add_line(1)

    # ファイル読込
    log(' - read')
    fm.read_file(file_path_test)
    log(' - readline')
    fm.readline_file(file_path_test)
    log(' - readlines')
    fm.readlines_file(file_path_test)
    log_add_line(1)

    # shelve（シェルフ：棚） +++++++++++++++++++++++
    # バイナリファイルとして一時的に保存が可能
    # shelveパッケージをインポートして利用する
    log(' - shelve')
    fm.save_shelve('condition', {'key1': 1, 'key2': 10})
    condition = fm.get_shelve('condition')
    log('SHELVE', condition)
    log_add_line()

    # pprint.pformat +++++++++++++++++++++++
    # Pythonでそのまま利用できる形でファイル保存が可能
    log(' - pprint.pformat -> file')
    sample_data = [{'key1': 'value1'}, {'key2': 'value2', 'key3': 'value3'}]
    # 後にimportするため、change directoryする前のスクリプト実行ディレクトリに配置する
    content_formated = 'sample_data_formatted = ' + pprint.pformat(sample_data) + ';\n'
    log('PPRINT.PFORMAT', content_formated)
    # このファイルを後ほどimportする
    filepath_format_test = os.path.dirname(dir_script) + '/pprint_test_data.py'
    fm.write_file(filepath_format_test, 'w', content_formated)
    log('import pprint.pformat file')
    # TODO 関数ないでインポートしたいがエラーとなる。要確認
    sample_data_formatted = pprint_test_data.sample_data_formatted
    log('AFTER IMPORT(ALL)', sample_data_formatted, title_space=20)
    log('AFTER IMPORT(0)', sample_data_formatted[0], title_space=20)
    log('AFTER IMPORT(0)', sample_data_formatted[1], title_space=20)
    log_add_line()

    # ファイル SEEK CHUNK +++++++++++++++++++++++
    log('>ファイル読み込み箇所指定、読み込み量指定')
    # 10文字目から10文字読み込む
    fm.seek(file_path_test, 10, 10)
    log_add_line()

    # CSV +++++++++++++++++++++++
    log('>CSV書き込み')
    import csv
    csv_test_dir = os.path.join(work_dir, 'csv_test')
    fm.makedir(csv_test_dir)
    csv_file_path = os.path.join(csv_test_dir, 'TEST.csv')
    with open(csv_file_path, 'w+') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name': 'A', 'Count': 1})
        writer.writerow({'Name': 'B', 'Count': 10})
        log('CSV CONTENT', csv_file.read())
        fm.seek(csv_file_path, 0)
    log_add_line(1)

    log('>CSV読み込み')
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            log('READ CSV ROW', row)
            log('READ CSV ROW[Name]', row['Name'])
            log('READ CSV ROW[Count]', row['Count'])
    log_add_line()
