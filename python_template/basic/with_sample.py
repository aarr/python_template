#!/usr/bin/env python3
"""With句の仕組み"""

import com.console

log = com.console.log
log_add_line = com.console.log_add_line

log('#============================')
log('# with句サンプル')
log('#============================')


class WithTest():
    """with句で利用できるクラス"""

    def __init__(self, name):
        """コンストラクタ

        Args:
            name (str): 名前
        """
        super().__init__()
        self.name = name

    def __enter__(self):
        """初期処理"""
        log('--- start ---')
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """終了処理

        Args:
            exception_type (str): エラータイプ
            exception_value (str): エラー値
            traceback (str): トレース

        Returns:
            WithTest: インスタンス
        """
        log('exception_type:{0}, exception_value:{1}, traceback:{2}'.format(
            exception_type, exception_value, traceback))
        log('--- end ---')
        log_add_line()
        return self


with WithTest('WITH TEST') as with_test:
    log(with_test.name)
    # 途中でエラーになろうと終了処理は正しく行われる
    raise Exception
