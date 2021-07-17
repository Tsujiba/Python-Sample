"""
#############################################################################
loopのスケジューリング
asyncio.call_soon:タスクをすぐに実行させる
asyncio.call_latar:タスクを遅延して実行させる
　→非同期させたい処理もコルーチンに対応させて記述しないと並行しない
 　例）await　~とか使う
#############################################################################
"""

import asyncio

# 非同期用のループオブジェクトを作成
loop = asyncio.get_event_loop()

def hello(name, loop):
    print('start')
    print('hello {}'.format(name))
    print('end')
    loop.stop()
    
if __name__ == '__main__':
    # 非同期処理
    loop.call_later(3, hello, 'Yu', loop)
    # loop.call_soon(hello, 'Das', loop)
    
    loop.run_forever()
    loop.close()