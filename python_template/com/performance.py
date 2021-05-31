#!/usr/bin/env python3
'''パフォーマンス測定用クラス
'''

import time

import com.console

log = com.console.log
log_add_line = com.console.log_add_line


class Performance():
    """パフォーマンス測定用クラス"""

    def __init__(self):
        """コンストラクタ"""
        super().__init__()
        self.initial_time = time.time_ns()
        self.times = {}
        self.marks = {}

    def mark(self, mark_name):
        """計測

        Args:
            mark_name (str): マーク名称
        """
        if mark_name is not None:
            self.times[mark_name] = time.time_ns()

    def mesure(self, process_name, start_mark=None, end_mark=None):
        """計測結果作成

        Args:
            process_name (str): 計測結果名称
            start_mark (str), optional): 計測開始マーク。未指定の場合、
            本クラスのインスタンスが生成されたタイミングを利用する. Defaults to None.
            end_mark (str, optional): 計測終了マーク。未設定の場合、
            本メソッドが呼ばれたタイミングを利用する。. Defaults to None.
        """
        start_time = self.times.get(start_mark, self.initial_time) if (
            start_mark is not None) else self.initial_time
        end_time = self.times.get(end_mark, time.time_ns()) if (
            end_mark is not None) else time.time_ns()
        self.marks[process_name] = {
            'name': process_name,
            'start_time': start_time,
            'duration': end_time - start_time
        }
        # log('[{0}] MESURE'.format(self.__class__.__name__), self.marks)

    def now(self):
        """現在の時刻を取得する

        Returns:
            int: epochからのnano秒を返却（Unixでは1970/1/1 0:0:0）
        """
        return time.time_ns()

    def get_entry(self, process_name):
        '''指定された処置結果名称の計測結果を返却する
        Args:
            process_name : 処理結果名称
        Returns:
            dict : 処理結果（詳細内容はget_entriesを参照）
                    指定された処理結果名称に対する結果が存在しない場合Noneとなる
        '''
        return self.marks.get(process_name)

    def get_entries(self):
        """全計測結果を返却する

        Returns:
            dict: キーが計測結果名称、値が計測結果のdictionaryを返却する。
                    計測結果には下記の情報を含む
                    name : 計測結果名称
                    start_time : 計測開始時刻
                    duration : 計測結果（nano秒）
        """
        return self.marks

    def get_simple_entries(self):
        """全計測結果を返却する

        Returns:
            dict : キーが計測結果名称、値は計測時間（ミリ秒）を返却する
        """
        return {process_name: result['duration']/(1000 * 1000)
                for process_name, result in self.marks.items()}
