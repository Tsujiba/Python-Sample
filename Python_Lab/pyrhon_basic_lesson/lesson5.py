"""This is review python course lesson"""


# 1　リスト型

list = [1, 2, 3, 4]
print(list)
print(__name__)

for l in list:
    print(l)

# 2 辞書型

d = {'daisuke': '25', 'Tsuyoshi': '19'}
print(d.keys())
print(d.values())
print(d.items())

for key, value in d.items():
    print(key, value)

# 3 enumerate関数→forループ内で連番をつけたい

i = 0
list = ['orange', 'apple', 'banana']
for l in list:
    print(i,':', l)
    i += 1

for i, l in enumerate(list):
    print(i, ':', l)

# 4 zip関数：複数リストを順番に取り出す

human = ['A', 'B', 'C']
old = ['15', '29', '16']
color = ['red', 'blue', 'orange']

for h, o, c in zip(human, old, color):
    print(h,':', o, ':', c)

#5 クロージャ：関数を後から柔軟に実行したい（固定で入れて、関数内関数の引数を後から指定して実行）

def area_circle(pi):
    def calc(radius):
        return pi * radius * radius
    return calcgit

cal1 = area_circle(3.14)
cal2 = area_circle(3.14159)

print(cal1(10))
print(cal2(10))
print(cal1(50))

# 6 デコレータ：関数に決まった処理を装飾する

# decorator1
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        f =func(*args, **kwargs)
        print('end')
        return f
    return wrapper

# @は利用するデコレータを宣言すれば
@print_info
def add_num(a, b):
    return a + b

result = add_num(10,20)
print(result)
