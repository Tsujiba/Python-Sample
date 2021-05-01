"""
#############################################################################
requests:サードパーティ製のパッケージ
　⇒urllibよりも簡単に利用可能（エンコードとか必要なし）
REST：HTTPメソッド　クライアントが行いたい処理をサーバに伝える
　・GET：データの参照
　・POST：データの新規登録
　・PUT：データの更新
　・DELETE：データの削除
#############################################################################

"""

import requests

payload = {'key1': 'value1', 'key2': 'value2'}

# GET
# r = requests.get('http://httpbin.org/get', params=payload)

# POST
# r = requests.post('http://httpbin.org/post', data=payload)

# PUT
# r = requests.put('http://httpbin.org/put', data=payload)

# DELETE
# r = requests.delete('http://httpbin.org/delete', data=payload)

# GET-timeout-option
r = requests.get('http://httpbin.org/get', params=payload, timeout=1)

print('ステータスコード:', r.status_code)
print(r.text)
print(r.json)

