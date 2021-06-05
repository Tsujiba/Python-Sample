"""
#############################################################################:
・collection.defaultdict
　 →dictionary
・
#############################################################################
"""

import collections

dict1 = {'a': 'a1', 'b': 'b', 'num': 0}
dict2 = {'b': 'bb', 'c': 'c'}
dict3 = {'b': 'bbb','c': 'cc', 'd': 'd'}

print(dict1)
# 重複している値は書き換える、新規は追加する
dict1.update(dict2)

print(dict1)
dict1.update(dict3)

print(dict1)

print('######################################################')

# collection.ChainMapを用いれば複数のディクショナリーをリストで管理できる
m = collections.ChainMap(dict1, dict2, dict3)

print(m)
print(m.maps)
print(m['a'])
m.maps.reverse()
print(m.maps)

