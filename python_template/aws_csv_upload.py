#!/usr/bin/env python3
'''CSV入出力サンプル
'''

from console import *
import file_operation
# ファイル書込
from io import StringIO
import sys, os, json ,csv, datetime, time
# boto3のWrappe
import aws

log('#============================')
log('# AWSアクセスサンプル')
log('#============================')
log('AWS ACCESS START')
# AWS接続定義取得
aws_config = aws.AwsConfig()

# S3アクセス
# ファイル読み取り
log('S3 READ FILE')
s3 = aws_config.generate_resource('s3')
BUCKET_NAME = 'dynamodb-external'
bucket = s3.Bucket(BUCKET_NAME)
obj = bucket.Object('table/2020-04-06-16-10-22/50b3ce91-269f-41f2-be01-08a1e8112354')
# binary
body = obj.get()['Body'].read()
log('S3 OBJECT', body)
# TEXT(JSON)
text_body = body.decode('utf-8')
log('S3 OBJECT TEXT', text_body)

# JSON->dict
# dict->CSV作成用データ
records = text_body.split('\n')
is_header_wrote = False
header = []
values = []
for index, record in enumerate(records):
    # 最後改行されて終わっている場合を考慮
    if len(record) == 0:
        break;
    record_dict = json.loads(record)
    log('S3 OBJECT REC {0}'.format(index), record_dict)
    temp_record = []
    for key  in record_dict.keys() :
        value = record_dict[key]
        log('CONTENT REC {0}'.format(index), 'KEY:{0}, VALUE:{1}'.format(key, value))
        if (is_header_wrote == False):
            header.append(key)
        # キーが型を表しており、毎回sであるので固定で取得
        temp_record.append(value['s'])
    is_header_wrote = True
    values.append(temp_record)
    log_add_line(1)
log_add_line()

log('HEADER', header)
log('RECORDS', values)
log_add_line()


# S3アクセス
# ファイル作成
# TODO：CSV化
log('S3 WRITE FILE')
S3_PATH= 'companyA'
now = datetime.datetime.fromtimestamp(time.time())
file_name = '{0}.csv'.format(now.strftime('%Y%m%d_%H%M%S'))
log('FILENAME', file_name)
with StringIO() as s: 
    # delimiter, quotingは必要なときに設定する
    writer = csv.writer(s, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    writer.writerows(values)
    upload_path = os.path.join(S3_PATH, file_name)
    s3.Object(BUCKET_NAME, upload_path).put(Body=s.getvalue())
log_add_line(1)


log('AWS ACCESS END')
