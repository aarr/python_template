#!/usr/bin/env python3
# mail.py
'''Mailサンプル
'''

from console import *
from email.mime.text import MIMEText
from email.header import Header
import sys, smtplib, file_operation
log('#============================')
log('# Mail')
log('#============================')
config_file_name = 'mail.config'
config_key = 'config'
config_key_address = 'address'
config_key_passwd = 'passwd'

def create_message(from_address, to_address, title, message):
    msg = {}
    msg['From'] = to_address
    msg['To'] = to_address


log('-------------------------------')
log('SEND MAIL START')
# 接続情報取得
if os.path.isfile(config_file_name) == False:
    if len(sys.argv) == 3:
        # ID,PASSを保存
        file_operation.save_shelve(config_key, 
        {   config_key_address : sys.argv[1] 
            ,config_key_passwd :sys.argv[2] 
        }, config_file_name)
    else:
        log('ERROR', '１度は引数（Mailアドレス、パスワード）を指定して実効してください')
        sys.exit()

smtp_server = 'smtp.gmail.com'
config = file_operation.get_shelve(config_key, config_file_name)
address = config[config_key_address]
passwd = config[config_key_passwd]

smtp_obj = smtplib.SMTP_SSL(smtp_server, 465)
result_ehlo = smtp_obj.ehlo()
log('EHLO', result_ehlo)
# Googleアカウントのセキュリティ設定（安全性の低いアプリへのアクセスの無効化）
# を変更しないとログインできない。
result_login = smtp_obj.login(address, passwd)
log('LOGIN', result_login)

charset = 'iso-2022-jp'
subject = 'テスト送信'
message = '''
Hello
SMTP TEST
こんにちは
さようなら
'''
msg = MIMEText(message, 'plain', charset)
msg['Subject'] = Header(subject.encode(charset), charset)

smtp_obj.sendmail(address, address, msg.as_string())
smtp_obj.quit()
log('SEND MAIL END')
log_add_line(2)

import imapclient, pyzmail, ssl
import backports.ssl
import pprint
log('-------------------------------')
log('RECIEVE MAIL START')
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True, ssl_context=context)
imap_obj.login(address, passwd)

# フォルダーの一覧を取得
list_forlder = imap_obj.list_folders()
log('FOLDERS')
log(pprint.pformat(list_forlder))

# フォルダーを指定
imap_obj.select_folder('INBOX', readonly=True)
# 検索を実行
# UITDs = imap_obj.search(['SINCE', '05-jul-2019'])
# Gmailの検索も利用可能
UITDs = imap_obj.gmail_search('from:order_acknowledgment@orders.apple.com')
log('UIDs', UITDs)
selected_uid = UITDs[len(UITDs) - 1]
row_message = imap_obj.fetch(selected_uid, ['BODY[]', 'FLAGS'])
log('ROW MESSAGE')
log(pprint.pformat(row_message))
log_add_line(1)
recieve_message = pyzmail.PyzMessage.factory(row_message[selected_uid][b'BODY[]'])
recieve_subject = recieve_message.get_subject()

# アドレス(from/to/cc/bcc)
log('FROM', recieve_message.get_address('from'))
# 件名
log('SUBJECT', recieve_subject)
# 本文
content = recieve_message.text_part.get_payload().decode(recieve_message.text_part.charset)
log('CONTENT', content)

log('RECIEVE MAIL END')