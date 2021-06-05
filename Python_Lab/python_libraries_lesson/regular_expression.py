"""
#############################################################################:
・正規表現：re
　　match():文字列の先頭で正規表現とマッチするか判定
　　search():文字列を操作して、正規表現がどこにマッチするか調べる
　　findall():正規表現にマッチする部分文字列を全て探し出しリストでかえす
　　finditer():重複しないマッチオブジェクトをイテレータでかえす
#############################################################################
"""

import re

# m = re.match('a.c', 'abc')
# print(m)
# print(m.group())

# m = re.search('a.c', 'test abc test abc')
# print(m)
# print(m.span())
# print(m.group())

# ?は前の文字が0か1回
# m = re.match('ab?', 'ab')
# m = re.match('ab*', 'a')
# m = re.match('ab+', 'ab')

# m = re.match('a{2,4}', 'aaaaa')
# m = re.match('[a-zA-Z0-9_]', 'a_AZ109')
# m = re.match('\w+', '_aaa')
# m = re.match('\W', '@')
# m = re.match('\d', '9')
# m = re.match('\s', ' ')

# m = re.match('\?', '?')
# m = re.match('^ab', 'abcd')
m = re.match('abc$', 'abctest abc')

print(m)

