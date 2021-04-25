"""config and Logging"""
"""
1.configParser
　How to use configparser
　コンフィグファイルの書き込み、読み込み
"""

import configparser

# config = configparser.ConfigParser()
#
# config['DEFALUT'] = {
#     'debug': True
# }
#
# config['web_Server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
#
# config['db_Server'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }
#
# with open('config.ini', 'w') as config_file:
#     config.write(config_file)

config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_Server']['host'])