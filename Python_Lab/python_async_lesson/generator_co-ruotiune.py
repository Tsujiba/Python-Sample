"""
#############################################################################
ジェネレーターのコルーチン：
コルーチン（英: co-routine）とはプログラミングの構造の一種。
サブルーチンがエントリーからリターンまでを一つの処理単位とするのに対し、コルーチンはいったん処理を中断した後、続きから処理を再開できる。 
接頭辞 co は協調を意味するが、複数のコルーチンが中断・継続により協調動作を行うことによる。
#############################################################################
"""

"""
# 普通にジェネレーター（復習）
def generator_hello():
    yield 'hello'
    yield 'hello'
    yield 'hello'

# for w in generator_hello():
#     print(w)
    
g = generator_hello()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""

"""
# ジェネレーターのコルーチン
def coroutine_generator_hello():
    while True:
        result = yield 'hello'
        yield result
    
g = coroutine_generator_hello()
print(next(g))
print(g.send('first'))
print(next(g))
print(g.send('second'))
"""

# yield fromで別のコルーチンからとってくる
def sub_generator_hello():
    yield 'hello1'
    yield 'hello2'
    yield 'hello3'
    return 'done'

def coroutine_generator_hello_2():
    while True:
        result = yield from sub_generator_hello()
        yield result
 
g = coroutine_generator_hello_2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

   
    