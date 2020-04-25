#!/usr/bin/env python3
'''AWSクライアント作成クラス
AWS lambdaなどで利用する場合、アクセスキー、シークレットキーは不要。
外部から実行する場合のキー情報を一度登録することで、２度目以降の実行時にキーの設定を不要とする。
キー情報を環境変数に登録しておくことで、不要とさせる事も可能
'''

import sys, os, boto3

# 別ディレクトリのため、パス追加
script_dir = os.path.abspath(__file__)
base_dir = os.path.join(os.path.dirname(script_dir), '..')
sys.path.append(os.path.join(base_dir, 'com'))

from console import *
import file_manager as file_operation

class AwsConfig():
    CONFIG_FILE_NAME = os.path.join(base_dir, 'config', 'aws.config')
    CONFIG_KEY = 'config'
    CONFIG_KEY_ACCESS_KEY = 'access_key'
    CONFIG_KEY_SECRET_KEY = 'secret_key'
    CONFIG_KEY_REGION = 'region'

    def __init__(self):
        '''Initializer'''
        super().__init__()
        print('CONFIGFILE:{0}'.format(self.CONFIG_FILE_NAME))
        if os.path.isfile(self.CONFIG_FILE_NAME) == False:
            print("アクセスキーを入力してください。")
            access_key = input()
            print("シークレットキーを入力してください。")
            secret_key = input()
            print("リージョンを入力してください。")
            region = input()
            config = {
                self.CONFIG_KEY_ACCESS_KEY: access_key,
                self.CONFIG_KEY_SECRET_KEY: secret_key,
                self.CONFIG_KEY_REGION: region
            }
            file_operation.save_shelve(self.CONFIG_KEY, config, self.CONFIG_FILE_NAME)
        # AWS認証情報を保持
        self.aws_config = file_operation.get_shelve(self.CONFIG_KEY, self.CONFIG_FILE_NAME)
    
    def __repr__(self):
        return None 
    
    def __str__(self):
        return None

    def generate_client(self, *args):
        '''指定されたタイプのクライアントを返却する
        '''
        return boto3.client(*args
            , aws_access_key_id = self.aws_config[self.CONFIG_KEY_ACCESS_KEY]
            , aws_secret_access_key = self.aws_config[self.CONFIG_KEY_SECRET_KEY]
            , region_name = self.aws_config[self.CONFIG_KEY_REGION])

    def generate_resource(self, *args):
        '''指定されたタイプのリソースを返却する
        '''
        return boto3.resource(*args
            , aws_access_key_id = self.aws_config[self.CONFIG_KEY_ACCESS_KEY]
            , aws_secret_access_key = self.aws_config[self.CONFIG_KEY_SECRET_KEY]
            , region_name = self.aws_config[self.CONFIG_KEY_REGION])


