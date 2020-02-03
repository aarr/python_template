#============================
# 正規表現
#============================
from console import *
log('#============================')
log('# 正規表現')
log('#============================')

import re
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

log(' - findall')
# ?で最短一致
regex_num_2_4 = re.compile(r'\d{2,4}?')
match = regex_num_2_4.search(text)
log('SEARCH(Match)', match.group())
match_array = regex_num_2_4.findall(text)
log('FINDALL', match_array)
log_add_line(1)

log(' - Flags')
# 大文字、小文字無視
regex_ignore_upper_lower = re.compile(r'm.', re.I)
log('IGNORE CASE OPTION(m.)', regex_ignore_upper_lower.findall(text))
log_add_line(1)

log(' - replace')
regex_sub_test = re.compile(r'([\w|\-]+)[ |\.]')
log('REPLACE(SUB)', regex_sub_test.sub(r'[\1]', text))
