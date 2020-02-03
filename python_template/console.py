def log(title, *messages, spacer=' ', title_space=15, title_sep=' : ', sep=' ', end='\n'):
    """ コンソールログ出力
    Args:
        title(str) : タイトル。指定が必須
        *messages(tuple, optional) : メッセージ。未指定の場合、titleのみ表示する
        title_sep(str, optional) : titleと*messagesの間のセパレータを指定可能
        title_space(int, optional) : titleから*messagesまでの空白の数
        sep(str, optional) : *messagesを文字列にする際のセパレータ
        end(str, optional) : 表示内容の最後に付与する文字

    Examples:
    >>> console.log('タイトル', '表示内容１', '表示内容２', title_space=10, title_sep=' | ', sep=' ')
    タイトル       | 表示内容１ 表示内容２

    """
    _message = None
    _message_length = len(messages)
    if _message_length == 1:
        _message = str(messages[0])
    elif _message_length > 1:
        # mapにてmessagesの中身をすべて文字列にする
        _message = sep.join(map(str, messages))
    _message = str(title).ljust(title_space, spacer) + title_sep + str(_message) if (_message != None) else str(title)
    print(_message, end=end)



def log_add_line(count=2) :
    """ 改行指定
    Args:
        count(int, optional) : 指定数文の改行をコンソールログ出力する。
    """
    indentStr = '' 
    # printで通常１つ改行が含まれるため、-１する
    for i in range(count - 1) :
        indentStr = indentStr + '\n'
    print(indentStr)

