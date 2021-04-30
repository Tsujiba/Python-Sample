import pickle

"""
#############################################################################
pickle：簡易的なデータ保存
　・pythonで作成したデータをファイルに保存（リスト、タプル、辞書型、オブジェクト）
 ※DBMSだとJavaなどのほかの言語でもデータを利用できるが、pickleはpythonだけ
#############################################################################

"""

class D(object):
    
    def __init__(self, name):
        self.name = name
        
data = {
    'a': [1, 2, 3],
    'b': ('test', 'apple'),
    'c': ['key', 'value'],
    'd': D('sample')
}

# pickleデータを作成
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# 読み込み

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded['a'])
    print(data_loaded['b'])
    print(data_loaded['c'])
    print(data_loaded['d'])
    print(data_loaded['d'].name)
    
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d'])) 

