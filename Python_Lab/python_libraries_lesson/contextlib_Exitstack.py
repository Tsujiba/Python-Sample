"""
#############################################################################:
・contextlib.ExitStack
　 →処理をスタックできる
  　一連の処理完了後に呼び出したい処理をスタックから実行
#############################################################################
"""

import contextlib


def is_ok_job():
    try:
        print('do something')
        # raise Exception
        return True
    except Exception:
        return False

def cleanup1():
    print('clean up1')

def cleanup2():
    print('clean up2')

def cleanup3():
    print('clean up3')

with contextlib.ExitStack() as stack:
    # 最後の呼び出す処理をスタックする
    stack.callback(cleanup1)
    stack.callback(cleanup2)
    stack.callback(cleanup3)
    
    is_ok = is_ok_job()
    if not is_ok:
        stack.pop_all()    
