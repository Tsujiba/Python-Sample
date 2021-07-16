"""
#############################################################################
asyncio.Lock:非同期処理のロック
　→非同期させたい処理もコルーチンに対応させて記述しないと並行しない
 　例）await lockを使う
#############################################################################
"""

import asyncio
import time

# 非同期用のループオブジェクトを作成
loop = asyncio.get_event_loop()

async def worker1(lock):
    print('worker1 start')
    async with lock:
        print('worker1 got lock')
        await asyncio.sleep(3)    
    print('worker1 end')
    
async def worker2(lock):
    print('worker2 start')
    async with lock:
        print('worker2 got lock')
        await asyncio.sleep(3)    
    print('worker2 end')

    
if __name__ == '__main__': 
    
    # 非同期処理
    lock = asyncio.Lock()
    loop.run_until_complete(asyncio.wait([worker1(lock),worker2(lock)]))
    loop.close()