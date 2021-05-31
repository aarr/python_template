"""CodeStyle Sample"""
# importの記載としては、組み込み、外部ライブラリ、自作の順で間を１行あける
# 記載順はアルファベット順
# 関数だけのimportはどこに実装されているものがわからないので、モジュールをimportする
# 大量のモジュールをimportする場合、パッケージの最初からimportする方がよい
# モジュール名で全てimportすると他のライブラリと強豪したり、内部の定義と強豪する。
import datetime
import time

import logging


logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s[%(name)s][%(levelname)s] %(message)s'
)
# グローバル変数は、大文字定義
LOGGER = logging.getLogger('ROBOTER')
LOGGER.setLevel(logging.DEBUG)


# クラス、関数の前後は2行開ける
# クラスはCamel形式
class StyleError(Exception):
    """StyleError

    Args:
        Exception (Exception): Extend Exception
    """
    pass


def _output_func_name_decorator(func):
    """関数名ログ出力デコレータ

    Args:
        func (function): 実行関数
    """
    def wrapper(*args):
        LOGGER.debug('-----START:{}-----'.format(func.__name__))
        func(*args)
        LOGGER.debug('------END:{}------'.format(func.__name__))
        LOGGER.debug('')
    return wrapper


# Generator
# sample_listとやっていることは同じ。パフォーマンスはGeneratorの方がよいので、
# GeneratorにできるものはGeneratorにする

# 関数、変数はSnake形式
def sample_generator(list_range):
    """Return Generator

    Args:
        list_range (num): range of list

    Yields:
        Generator: generator
    """
    for value in range(list_range):
        yield value


def sample_list(list_range):
    """Return list

    Args:
        list_range (num): range of list

    Returns:
        list: list
    """
    num = []
    for value in range(list_range):
        num.append(value)
    return num


@_output_func_name_decorator
def measure_performance_of_generator(func):
    """Generatorパフォーマンス測定

    Args:
        func ([type]): [description]
    """
    # Generator
    start_time_generator = time.time()
    for value in sample_generator(1000000):
        if value % 100000 == 0:
            func(value)
    end_time_generator = time.time()
    LOGGER.debug('{} msec'.format(end_time_generator - start_time_generator))
    # list
    LOGGER.debug('List')
    start_time_list = time.time()
    for value in sample_list(1000000):
        if value % 100000 == 0:
            func(value)
    end_time_list = time.time()
    LOGGER.debug('{} msec'.format(end_time_list - start_time_list))


@_output_func_name_decorator
def do_ternary_operator():
    """三項演算子実行サンプル"""
    # 複雑な式は書かない
    now = datetime.datetime.now()
    y = now.second
    x = y if int(y) >= 30 else 0
    LOGGER.debug('x is {}, y is {}'.format(x, y))


@_output_func_name_decorator
def arg_default_sample_for_list(default_list1=None, default_list2=[]):
    """リスト引数サンプル

    Args:
        default_list1 (list, optional): リスト引数. Defaults to None.
        default_list2 (list, optional): リスト引数（バグ温床）. Defaults to [].
    """
    # リストの引数デフォルト値
    # 空のリストを入れない。参照渡しのため問題あり（呼び出しもとで値の書き換えが可能）
    # 下記のように初期処理で初期化する
    if default_list1 is None:
        default_list1 = []
    default_list1.append('10')
    default_list2.append('10')

    LOGGER.debug('LIST1:')
    LOGGER.debug(default_list1)
    LOGGER.debug('LIST2:')
    LOGGER.debug(default_list2)


# 直接実行対応
# importのときではなく、直接実行されたときの処理を定義する
if __name__ == '__main__':
    # lambda利用
    # 処理内容が単純であれば、関数定義よりもコードがシンプルになるためよい
    measure_performance_of_generator(lambda value: LOGGER.debug(value))

    # 三項演算子
    do_ternary_operator()

    # LIST引数定義のバグ
    # 複数回呼び出すことで想定外の挙動（実行数分リスト内容が増えている）
    arg_default_sample_for_list()
    arg_default_sample_for_list()
