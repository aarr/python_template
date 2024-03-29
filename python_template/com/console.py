#!/usr/bin/env python3
"""Console Logger
コンソールにログ出力する
"""
import os
import logging

LOG_DIR = os.path.join(os.path.dirname(__file__), 'log')
try:
    os.makedirs(LOG_DIR)
except FileExistsError as error:
    print('log directory is exists : {0}'.format(LOG_DIR))
    print(error)
else:
    print('make log directory : {0}'.format(LOG_DIR))

logging.basicConfig(
    # ファイル出力の場合コメントアウト解除
    # filename=os.path.join(LOG_DIR, 'applicationl.log'),
    # その他のパッケージのログはERROR
    level=logging.ERROR,
    format='%(asctime)s[%(levelname)s] %(message)s'
)
# basicConfigで設定している内容から、設定を一部変更して利用したい場合LOGGERを定義する
# basicConfig通り利用する場合は、定義する必要はない
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def debug(message):
    '''debugLog
    '''
    LOGGER.debug(message)


def warn(message):
    '''warningLog
    '''
    LOGGER.warn(message)


def error(message):
    '''errorLog
    '''
    LOGGER.error(message)


def disableLogging(level=logging.CRITICAL):
    '''ログの無効化
    '''
    logging.disable(level)


def format_message(title, *messages, spacer=' ', title_space=15,
                   title_sep=' : ', sep=' '):
    """ メッセージフォーマット
    Args:
        title(str) : タイトル。指定が必須
        *messages(tuple, optional) : メッセージ。未指定の場合、titleのみ表示する
        title_sep(str, optional) : titleと*messagesの間のセパレータを指定可能
        title_space(int, optional) : titleから*messagesまでの空白の数
        sep(str, optional) : *messagesを文字列にする際のセパレータ
    Returns:
        str : フォーマット済み文字列

    Examples:
    >>> console.format_message('タイトル', '表示内容１', '表示内容２',
                               title_space=10, title_sep=' | ', sep=' ')
    タイトル       | 表示内容１ 表示内容２

    """
    _message = None
    _message_length = len(messages)
    if _message_length == 1:
        _message = str(messages[0])
    elif _message_length > 1:
        # mapにてmessagesの中身をすべて文字列にする
        _message = sep.join(map(str, messages))
    _message = str(title).ljust(title_space, spacer) + title_sep + str(_message) if (_message is not None) else str(title)
    return _message


def log(title, *messages, spacer=' ', title_space=15,
        title_sep=' : ', sep=' ', end='\n'):
    """ コンソールログ出力
    Args:
        title(str) : タイトル。指定が必須
        *messages(tuple, optional) : メッセージ。未指定の場合、titleのみ表示する
        title_sep(str, optional) : titleと*messagesの間のセパレータを指定可能
        title_space(int, optional) : titleから*messagesまでの空白の数
        sep(str, optional) : *messagesを文字列にする際のセパレータ
        end(str, optional) : 表示内容の最後に付与する文字

    Examples:
    >>> console.log('タイトル', '表示内容１', '表示内容２',
                     title_space=10, title_sep=' | ', sep=' ')
    タイトル       | 表示内容１ 表示内容２

    """
    # *messagesで、format_messageにわたすことで、tupleを展開して渡すことが可能
    # messagesで渡すとtupleの入れ子になる。
    # print(format_message(title, *messages, spacer=spacer,
    #       title_space=title_space, title_sep=title_sep, sep=sep), end=end)
    debug(format_message(title, *messages,
                         spacer=spacer, title_space=title_space,
                         title_sep=title_sep, sep=sep))


def log_add_line(count=2):
    """ 改行指定
    Args:
        count(int, optional) : 指定数文の改行をコンソールログ出力する。
    """
    indentStr = ''
    # printで通常１つ改行が含まれるため、-１する
    for i in range(count):
        # indentStr = indentStr + '\n'
        debug(indentStr)
    # print(indentStr)
