"""
#############################################################################
flask:flaskのテスト用クライアントプログラム
#############################################################################
"""

import requests

"""
test01
"""

# payload1 = {'username': 'Tsujiba'}

# GET
# r = requests.get('http://127.0.0.1:5000/get', params=payload1)

# POST
# r = requests.post('http://127.0.0.1:5000/post', data=payload1)

# PUT   
# r = requests.put('http://127.0.0.1:5000/put', data=payload1)

# DELETE
# r = requests.delete('http://127.0.0.1:5000/delete', data=payload1)

"""
test02
"""
payload2 = {'name': 'Tsujiba'}

# GET
# r = requests.get('http://127.0.0.1:5000/employee', params=payload2)

# POST
r = requests.post('http://127.0.0.1:5000/employee', data=payload2)

# PUT   
# r = requests.put('http://127.0.0.1:5000/employee', data={'name': 'Tsujiba', 'new_name': 'Yamada'})

# DELETE
# r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'Yamada'})

print(r.text)