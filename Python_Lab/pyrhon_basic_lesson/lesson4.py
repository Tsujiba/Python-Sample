
"""
file operation and system
"""

"""
file create
"""
#
# f = open('test.txt', 'w')
# f.write('test')
# f.close()

# Use with statement
#
# s = """\
# ABC
# DEF
# GHI
# JKL
# """

# with open('test.txt', 'w') as f:
#     f.write(s)

# with open('test.txt', 'r') as f:
#     contents = f.read(3)
#     print(contents)
#
#     contents = f.read(4)
#     print(contents)
#
# with open('test.txt', 'r') as f:
#     while True:
#         line = f.readline()
#         print(line)
#         if not line:
#             break

"""
templete
1.import string
2.string.Templete
"""
#
# import string
#
# # s = """/
# # Hello $name
# # $animal is good!!
# # Hava a nice day
# # """
# #
# # t = string.Template(s)
# # contents = t.substitute(name='Yu', animal='dog')
# # print(contents)
#
# with open('Design/design.txt') as f:
#     t = string.Template(f.read())
#
# contents = t.substitute(name='Kiyoshi', animal='Cat')
# print(contents)


"""
csv write and read
"""

# import csv
#
# with open('test.csv', 'w', newline="") as cav_file:
#     fieldnames = ['Name', 'Number']
#     writer = csv.DictWriter(cav_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name': 'A', 'Number': 1})
#     writer.writerow({'Name': 'B', 'Number': 2})
#
# with open('test.csv', 'r', newline="") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print

"""
file operation
"""
#
# import os
# import pathlib
# import glob
# import shutil
#
# # file is exist or not exist
# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('Design'))
#
# # os.rename('test.txt', 'renamed.txt')
#
# # linkfile creates as shotcut file
# # os.symlink('renamed.txt', 'symlink.txt')
#
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')
#
# # os.mkdir('test_dir')
# # os.mkdir('test_dir/test_dir2')
# # print(os.listdir('test_dir'))
# # pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# # shutil.copy('test_dir/test_dir2/empty.txt',
# #             'test_dir/test_dir2/empty2.txt')
# #
# # print(glob.glob('test_dir/test_dir2/*'))
#
# # shutil.rmtree('test_dir')
#
# print(os.getcwd())

"""
tar zip
tempfile
"""

import os
import tarfile
import zipfile
import tempfile

# os.mkdir('test_dir')
# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('test_dir')

# tempfile delete after run
# with tempfile.TemporaryFile(mode='w+') as t:
#     t.write('hello')
#     t.seek(0)
#     print(t.read())

"""
subprocess 
command execution
"""

# import subprocess

# os.system('dir')
# subprocess.run(['dir'])
# subprocess('dir', shell=True, check=True)

"""
datetime
"""

# import datetime
#
# now = datetime.datetime.now()
# print(now)
# print(now.isoformat())
# print(now.strftime('%Y/%m/%d-%H_%M_%S_%f'))
# print(now.strftime('%y/%m/%d-%H_%M_%S_%f'))
#
# today = datetime.date.today()
# print(today)
# print(today.isoformat())
# print(today.strftime('%y/%m/%d'))
#
# t = datetime.time(hour=1, minute=5, second=10, microsecond=100)
# print(t)
# print(t.isoformat())
# print(t.strftime(('%H_%M_%S_%f')))
#
# print(now)
# d = datetime.timedelta(weeks=-1)
# d = datetime.timedelta(days=365)
# print(now - d)
#
# import time
# print('################')
# time.sleep(3)
# print('################')
#
# import os
# import shutil
# # example: file backup
#
# filename = 'test.txt'
#
# if os.path.exists(filename):
#     shutil.copy(filename, "{}.{}".format(
#         filename, now.strftime('%Y_%m_%d')))
#
# with open('test.txt', 'w') as text:
#     text.write('test')