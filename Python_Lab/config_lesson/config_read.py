import configparser

"""
コンフィグファイルを読み込むプログラム
"""

config = configparser.ConfigParser()
config.read('config_lesson\config.ini')
print(config['PROFILE']['name'])
print(config['PROFILE']['age'])
print(config['PROFILE']['occupation'])
print(config['SAMPLE']['ip'])