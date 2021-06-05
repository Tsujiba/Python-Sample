"""
#############################################################################:
・contextlib.contextmanager,decoratar
　・デコレータでやっていた複雑な処理を簡単で分かりやすく記述できる
#############################################################################
"""

import contextlib

"""
decorator
↓は複雑。。。。

def tag(name):
    def _tag(f):
        def _wrapper(content):
            print('<{}>'.format(name))
            r = f(content)
            print('<{}>'.format(name))
            return r
        return _wrapper
    return _tag

@tag('h2')
def f(content):
    print(content)

f('test')
"""

"""
contextlib
"""

@contextlib.contextmanager
def tag1(name):
    print('<{}>'.format(name))
    yield
    print('<{}>'.format(name))


# 上記と同じ処理をcontextDecoratorを用いて記述したもの
class tag2(contextlib.ContextDecorator):
    
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print('<{}>'.format(self.name))

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print('<{}>'.format(self.name))


@tag1('h2')
def f1(content):
    print(content)

@tag2('h3')
def f2(content):
    raise Exception('error')
    print(content)

f1('test')
f2('test2')
