#!/usr/bin/env python3
'''HTTPリクエストテスト
API GATEWAY
    マッピングテンプレートで利用できパラメータ郡
    https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html
    マッピングテンプレートの使い方
    https://qiita.com/tamura_CD/items/ca8e531f74ea5b82a5b7

    TODO
    タイムアウトじのハンドリング
    lambda側での実装になるが、リダイレクトURLの返却（302）
'''

from console import *
import file_operation
import urllib.request, urllib.parse, os, sys, json

config_file_name = 'awsapi.config'
config_key = 'config'
config_key_url = 'url'
config_key_api_key = 'api_key'


def do_get(url, params, headers):
    '''GET実行
    '''
    log('GET START')

    query_string = urllib.parse.urlencode(params)
    log('QUERY STRING', query_string)

    req = urllib.request.Request('{}?{}'.format(url, query_string), None, headers)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            log('RESULT', body)
    except urllib.request.HTTPError as ex:
        log('ERROR', ex)
    finally:

        log('GET END')

def do_post(url, params, headers):
    '''POST実行
    '''
    log('POST START')

    json_param = json.dumps(params).encode()
    #json_param = urllib.parse.urlencode(params).encode('utf-8')
    log('PARAM', json_param)

    req = urllib.request.Request(url, json_param, headers)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            log('RESULT', body)
    except urllib.request.HTTPError as ex:
        log('ERROR', ex)
    finally:
        log('POST END')


log('#============================')
log('# HTTP')
log('#============================')
log('HTTP Request start')
# 入力チェック
args = sys.argv;
if os.path.isfile(config_file_name) == False and len(args) != 3:
    log('ERROR', '１度は引数（URL、APIきー）を指定して実効してください')
    sys.exit()
if len(args) == 3:
    config = {
        config_key_url: args[1],
        config_key_api_key: args[2]
    }
    file_operation.save_shelve(config_key, config, config_file_name)
elif os.path.isfile(config_file_name) == False:
    log('ARGUMENTS ERROR', '引数の個数が正しくありません。URL、APIキーを指定してください')
    sys.exit()
    
# ---------------------
# リクエストパラメータ定義
# ---------------------
config = file_operation.get_shelve(config_key, config_file_name)
url = config[config_key_url]
api_key = config[config_key_api_key]
params = {
    'id' : '1'
    ,'ymd' : '20200101'
}
# apiキーをAPI GATEWAYに設定したため、x-api-key未設定の場合、403エラーとなる
headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key
}

# GET実行
do_get(url, params, headers)
log_add_line(1)

# POST実行
do_post(url, params, headers)

log('HTTP Request end')
