
def is_isbn_or_key(word):
    """
        # isbn13  13位0-9数字组成
        # isbn10  部分‘_'和10个0-9数字
        :return: 返回key or isbn
        """
    is_keyword = 'key'
    if len(word) == 13 and word.isdigit():
        is_keyword = 'isbn'
    short_word = word.replace('_', '')
    if '_' in word and len(short_word) == 10 and short_word.isdigit():
        is_keyword = 'isbn'
    return is_keyword