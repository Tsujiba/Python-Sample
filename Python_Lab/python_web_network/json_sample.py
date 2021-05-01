"""
#############################################################################
JSONを作成、読みこむ

#############################################################################

"""

import json

json_data = {
    'employee':
        [
            {'id': 111, 'name': 'Tsujiba'},
            {'id': 222, 'name': 'Kagawa'}
        ]
}

# JSON変換前の出力
print('############################################')
print(json_data)

# JSON変換後の出力（python上で）
print('############################################')
a = json.dumps(json_data)
print(a)

# JSONファイルへの出力
print('############################################')
with open('test.json', 'w') as f:
    json.dump(json_data, f)

# JSONファイルの読みこむ
print('############################################')
with open('test.json', 'r') as f:
    load_data = json.load(f)
    print(load_data)
    
    for person in load_data['employee']:
        print(person)





