#!/usr/bin/env python3
# web_scraping.py
'''Webスクレイピングサンプル
'''

import webbrowser, requests, sys, os 
from console import *
from file_operation import *

log('#============================')
log('# WEB SCRAPING')
log('#============================')
log(' - WEBBROWSER')
address = 'https://github.com/oreilly-japan/automatestuff-ja' 
webbrowser.open(address)
log_add_line(1)


log(' - REQUESTS')
home = os.path.expanduser('~')
work_dir = os.path.join(home, 'work_python', 'web_scraping_test')
makedir(work_dir)
log('WORKDIR', work_dir)
# リクエスト送信
res = requests.get(address)
res.raise_for_status()
save_file_path = os.path.join(work_dir, 'save_file')
save_file = make_file(save_file_path, 'wb')
if save_file != None:
    for chunk in res.iter_content(100 * 1000):
        save_file.write(chunk)
    save_file.close()
    log('REQUEST', 'COMPLETE : {0}'.format(address))


log(' - HTML解析:BeautifulSoup')
import bs4
# requestsの結果から直接解析
no_starch_soup = bs4.BeautifulSoup(res.text)
log('TYPE', type(no_starch_soup))
try:
    # 保存されているファイル（html）から解析
    save_file = make_file(save_file_path, 'r+')
    save_file_soup = bs4.BeautifulSoup(save_file)
    log('TYPE', type(save_file_soup))
    # CSSセレクタで要素の中を検索可能
    divs= save_file_soup.select('div')
    log('DIV', divs)
finally:
    if save_file != None:
        save_file.close()
