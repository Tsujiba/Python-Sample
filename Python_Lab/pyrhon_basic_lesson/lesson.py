"""
name = 'Yu'
family = 'Tsujibayashi'

print(f'My name is {name} {family}.')

"#######################"

list_01 = [1, 2, 3, 4]
print(list_01)
print(list_01[::-1])

print('###############################')

list_01.append(5)
list_01.pop()
list_01.remove(2)
print(list_01)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
a += b

c = [11, 12, 13]

a.extend(c)
print(a)

print('###############################')

d = [1, 3, 7, 3, 4, 1, 7]
print(d.index(1))
print(d.index(1, 1))
print(d.count(3))

e = 'My name is Yu Tsujibayashi'
to_split = e.split(' ')
print(to_split)

f = ' '.join(to_split)
print(f + '.')

# リストのコピーは参照渡しなので注意
# 下記ではa,bも最初が100になる
a = [1, 2, 3, 4]
b = a
a[0] = 100
print('a =', a)
print('b = ', b)

# それだはどうするか？→copy関数をつかう
a = [1, 2, 3, 4]
b = a.copy()
a[0] = 100
print('a =', a)
print('b = ', b)

# tapple is immutable
a = (1, 2, 5)
print(type(a))

a = (1,)
print(type(a))

# taple unpacking

a = (10, 20)
x, y = a
print(x, y)

# exchange var by using taple unpacking

a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

# dictionary type

d = {'a': 10, 'b': 20}
print(d)
print(d['a'])

# dictionary method

# print(help(dict))
print(d.keys())
d2 = {'a': 100, 'c': 45}
print(d, d2)
d.update(d2)
print(d)
d.pop('a')
print(d)
d.clear()
print(d)

# 集合型
A_friends = {'Tsujiba', 'Kana', 'Risa', 'Yoshida'}
B_friends = {'Tsujiba', 'Tanaka', 'Risa', 'Lrona'}

print(A_friends & B_friends)

# リストを集合型へ変換

My_List = ['apple', 'orange', 'soda', 'orange']
r = set(My_List)
print(r)



ans = -2
if ans > 0:
    print('positive')
elif ans == 0:
    print('zero')
else:
    print('negative')

ans2 = 2

if ans > 0 and ans2 > 0:
    print('double positive')
else:
    print('No positive')

# l = 0
# while l < 5:
#    print(l)
#    if l % 2 == 0:
#        print('2dewaremasu')
#    l += 1

for i in range(1, 10, 2):
    print(i)

# i is not used in forloop
for _ in range(10):
    print('Hey')

fruit = ['apple', 'banana', 'orange']
days = ['Mon', 'Tue', 'Web']
# for i, fruit in enumerate(fruit):
#    print(i, fruit)

for f, d in zip(fruit, days):
    print(f, d)

# dictionary for loop
di2 = {'x': 100, 'y': 200}

for k, v in di2.items():
    print(k, ':', v)


# 関数定義,
def add_num(a=0, b=2):
    return a + b


r = add_num()
print(r)
r = add_num(3, 6)
print(r)


# tupple hikisuu
def sample_def(word, *args):
    print('word=', word)
    for arg in args:
        print(arg)


sample_def('start', 'Hey', 'you', 'fight')


# 辞書引数

def sample_def2(word, *args, **kwargs):
    print(word)
    print(args)
    print(kwargs)


sample_def2('start', 'boy', 'girl', key='keys', value='values')


# How to closure

def circle_area(pi):
    def calc(radius):
        return pi * radius * radius

    return calc


f1 = circle_area(3.14)
f2 = circle_area(3.14159)

print(f1(10))
print(f2(10))


# How to use Decorator

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)

    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        resurt = func(*args)
        print('end')
        return resurt

    return wrapper


@print_info
@print_more
def add_num(num1, num2):
    return num1 + num2


print(add_num(5, 5))
# print(add_num(2, 5))

# lambda
weekList = ['mon', 'Tue', 'Web', 'thu', 'Fri', 'sat', 'Sun']


def changeStr(words, func):
    for word in words:
        print(func(word))


changeStr(weekList, lambda word: word.capitalize())
changeStr(weekList, lambda word: word.lower())

# for l in weekList:
#     print(l)

# リスト内含合

l2 = [0, 1, 2, 3, 4]

l3 = [l for l in l2 if l % 2 == 0]
print(l3)
"""


# Exception
#
# l = [0, 1, 2, 3, 4]
# i = 5
#
# try:
#     print(l[0])
# except IndexError as ex:
#     print("Error:{}".format(ex))
#
# except NameError as ex:
#     print("Error:{}".format(ex))
# else:
#     print('done')
# finally:
#     print('clean up!!')

# Unique Exception

class tsujibaExcption(Exception):
    pass

def check():
    namelist = ['tanaka', 'tsujiba', 'nishi']

    for l in namelist:
        if l == 'tsujiba':
            raise tsujibaExcption
        print(l)

try:
    check()
except tsujibaExcption as ex:
    print('Error')