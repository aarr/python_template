#!/usr/bin/env python3
# sms.py
'''SMS送信サンプル
'''
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import sys, os

# 別ディレクトリのため、パス追加
script_dir = os.path.abspath(__file__)
base_dir = os.path.join(os.path.dirname(script_dir), '..')
sys.path.append(os.path.join(base_dir, 'com'))

from console import *
import file_manager as file_operation

log('#============================')
log('# SMS')
log('#============================')
log('SMS START')
config_file_name = os.path.join(base_dir, 'config', 'sms.config')
config_key = 'config'
config_key_address = 'address'
config_key_passwd = 'passwd'

# 入力チェック
args = sys.argv;
log('CURRENT DIR', os.getcwd())
if os.path.isfile(config_file_name) == False and len(args) != 5:
    log('ERROR', '１度は引数（送信番号、SID、AUTH_TOKEN、受信番号）を指定して実効してください')
    sys.exit()
if len(args) == 5:
    config = {
        'number' : args[1],
        'sid' : args[2],
        'auth_token' : args[3],
        'receive_number' : args[4]
    }
    file_operation.save_shelve(config_key, config, config_file_name)
elif os.path.isfile(config_file_name) == False:
    log('ARGUMENTS ERROR', '引数の個数が正しくありません。送信番号、SID、AUTH_TOKEN、受信番号の４つを指定してください')
    sys.exit()

# SMS送信時に必要なパラメータ
config = file_operation.get_shelve(config_key, config_file_name)
number = config['number']
account_sid = config['sid']
auth_token = config['auth_token']
receive_number = config['receive_number']

log('NUMBER', number)
log('ACCOUNT_SID', account_sid)
log('AUTH_TOKEN', auth_token)
log('RECIVE_NUMBER', receive_number)

client = Client(account_sid, auth_token)
try:
    message = client.messages.create(body='Hello from python', from_=number, to=receive_number)
    log('MESSAGE', message)
    log_add_line(1)
except TwilioRestException as ex:
    log('ERROR', ex)
    sys.exit()

# messageの内容確認
# 実際はメッセージ送信前にmessage取得している為、正しい状態は取得できない。
# 正しい状態を取得するためには、messageを取得しなおす必要がある。
log('STATUS', message.status)
log('DATE', message.date_created)
log('DATE_SENT', message.date_sent)
log_add_line(1)
# message再取得
log('SID', message.sid)
updated_message = client.messages.get(message.sid)
log('CONTEXT', updated_message)
# 何故か属性が存在問ウエラーが発生する
# log('STATUS', updated_message.status)
# log('DATE', updated_message.date_created)
# log('DATE_SENT', updated_message.date_sent)
log('SMS END')