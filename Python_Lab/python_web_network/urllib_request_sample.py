"""
#############################################################################
REST：HTTPメソッド　クライアントが行いたい処理をサーバに伝える
　・GET：データの参照
　・POST：データの新規登録
　・PUT：データの更新
　・DELETE：データの削除
#############################################################################

"""

import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

# GETメソッド
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)
with urllib.request.urlopen(url) as f:
    r = f.read().decode('utf-8')
    print(json.loads(r))


# POSTメソッド
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request('http://httpbin.org/post', data=payload, method='POST')

with urllib.request.urlopen(req) as f:
    r = f.read().decode('utf-8')
    print(json.loads(r))


# PUTメソッド
req = urllib.request.Request('http://httpbin.org/put', data=payload, method='POST')

with urllib.request.urlopen(req) as f:
    r = f.read().decode('utf-8')
    print(json.loads(r))

# DELETEメソッド
req = urllib.request.Request('http://httpbin.org/delete', data=payload, method='POST')

with urllib.request.urlopen(req) as f:
    r = f.read().decode('utf-8')
    print(json.loads(r))
    
    
