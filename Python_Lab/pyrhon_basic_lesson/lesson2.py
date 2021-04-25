# import sys
# from lesson_package import utils

"""
How to use commandline value
1.import sys
2.sys.args is list has commandline value
"""
# print(sys.argv)
#
# for i in sys.argv:
#     print(i)

"""
How to use package.function
1.make package(directory) concluding xxxx.py... and __init__.py that is essential
2.import package
3.another discription is from {packagename} import {modulename}
"""
# import lesson_package.utils

# # ans = lesson_package.utils.hello_tsujiba('Say!')
# ans = utils.hello_tsujiba('Say!')
# print(ans)

"""
How to use import *
However import * isn't recommended
Because * isn't accurate for developer what module is imported
If you use "import *",
Attention!!-> make __all__ = [modulename...] 
"""
# from lesson_package.talks import animal
# from lesson_package.talks import human
# from lesson_package.talks import *
#
# human.say_hello()
# human.say_tsujiba()
# animal.say_hello()
# animal.say_tsujiba()

"""
python builtins　function
URL:https://docs.python.org/ja/3/library/functions.html
"""
#
# ranking = {'A':20, 'B':57, 'C':30 }
#
# # sorted is builtins function that is often used.
# print(sorted(ranking))
# print(sorted(ranking, key=ranking.get))
# print(sorted(ranking, key=ranking.get, reverse=True))

"""
python standard libraray is need to import
pip install is not needed
URL:https://docs.python.org/ja/3/library/index.html
"""

# from collections import defaultdict
#
# s = "gajglkajglsjgsglg"
#
# d = defaultdict(int)
#
# for c in s:
#     d[c] += 1
# print(d)

"""
thirdparty library
URL:https://pypi.org/
pip install is needed
for example 'pip install termcolor'
"""
#
# from termcolor import colored
#
# print(colored('test', 'red'))

"""
import discription rule
1.standard->2.thirdparty->my_package->4.my_loacl_file
2.alphabetical sorted is good in each section
3. __file__ indicates path
4.syspath is order or path that python read
"""

# import collections
# import os
# import sys
#
# import termcolor
#
# import lesson_package
#
# import lesson
#
# print(collections.__file__)
# print(termcolor.__file__)
# print(sys.path)

"""
How to use __name__ and __main__
import file is executed when it is imported
"""
# #
# import config
#
# # __main__
# print(__name__)
#
# # good when app is developed
#
# import lesson_package.talks.animal
#
# def main():
#     lesson_package.talks.animal.say_tsujiba()
#
# if __name__ == '__main__':
#     main()