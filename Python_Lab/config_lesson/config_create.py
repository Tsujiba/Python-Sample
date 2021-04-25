import configparser

"""
コンフィグファイルを作成するプログラム
作成したいコンフィグファイルは下記である
[PROFILE]
name = tsujiba
age = 26
occupation = engineer

[SAMPLE]
time = 60
ip = 127.0.0.1
port = 443
"""

config = configparser.ConfigParser()
config['PROFILE'] = {
    'name':'tsujiba',
    'age': 26,
    'occupation': 'engineer'
}

config['SAMPLE'] = {
    'time': 60,
    'ip': '127.0.0.0',
    'port': 443
    }

with open('config.ini', 'w') as config_file:
    config.write(config_file)
    
