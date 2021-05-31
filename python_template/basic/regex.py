#!/usr/bin/env python3
# regex.py
# 

""" 正規表現
正規表現サンプル集
"""
import re

import com.console

log = com.console.log
log_add_line = com.console.log_add_line

log('#============================')
log('# 正規表現')
log('#============================')

# 基本 +++++++++++++++++++++++
# RAWを渡す方が正規表現の内容をエスケープする必要がない
log('> re 使い方')
log(' - search')
text = 'My number is 090-1234-5678.'
regex_phone_num = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
match = regex_phone_num.search(text)
log('REGEXP ALL', match.group())
log('REGEXP GROUP(0)', match.group(0))
log('REGEXP GROUP(1)', match.group(1))
log('REGEXP GROUP(2)', match.group(2))
log('REGEXP GROUP(3)', match.group(3))
log_add_line(1)

# 全一致 +++++++++++++++++++++++
log(' - findall')
# ?で最短一致
regex_num_2_4 = re.compile(r'\d{2,4}?')
match = regex_num_2_4.search(text)
log('SEARCH(Match)', match.group())
match_array = regex_num_2_4.findall(text)
log('FINDALL', match_array)
log_add_line(1)

# 置換 +++++++++++++++++++++++
log(' - sub(replace)')
regex_sub_test = re.compile(r'([\w|\-]+)[ |\.]')
log('REPLACE(SUB)', regex_sub_test.sub(r'[\1]', text))
log_add_line(1)

# オプション +++++++++++++++++++++++
log(' - Flags')
# 大文字、小文字無視
regex_ignore_upper_lower = re.compile(r'm.', re.I)
log('IGNORE CASE OPTION(m.)', regex_ignore_upper_lower.findall(text))
log_add_line(1)
log(' compileの引数は２つ。複数指定する場合は「|」で結合する')
test_text = '''
My number is 090-1234-5678.
Your number is 080-9876-4321.
'''
regex_ignore_single_flg = re.compile(r'm.|.Y', re.I)
# re.S(DOTALL)は「.」で改行も含める
regex_ignore_multi_flg = re.compile(r'm.|.Y', re.I | re.S)
regex_ignore_single_flg = re.compile(r'm.|.Y', re.I)
log('SINGLE FLAS', regex_ignore_single_flg.sub(r'[CHANGE]', test_text))
log('MULTI FLAG', regex_ignore_multi_flg.sub(r'[CHANGE]', test_text))
log_add_line(1)

# tips +++++++++++++++++++++++
log(' - 複雑な正規表現の記述')
phone_regex_text = r'''(
    (\d{3}|\(\d{3}\))?  # 3桁市外局番。()付きも考慮
    (\s|-|\.)?          # 区切り文字（space/-/.のいずれか）
    (\d{3})             # 3桁市内局番
    (-s|-|\.)           # 区切り
    (\d{4})             # 4桁の番号
    (\s*(ext|x|ext.)\s\*\d{2,5})? # 2〜5桁の内線番号
)'''
log(phone_regex_text)
phone_regex = re.compile(phone_regex_text, re.VERBOSE)
phone_match_array = phone_regex.findall('090-123-4567ext890')
log(phone_match_array)
