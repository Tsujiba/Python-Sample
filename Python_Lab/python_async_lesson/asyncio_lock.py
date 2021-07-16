"""
#############################################################################
asyncio:非同期処理
　→非同期させたい処理もコルーチンに対応させて記述しないと並行しない
 　例）await　~とか使う
#############################################################################
"""

import asyncio
import threading
import multiprocessing
import time

# 非同期用のループオブジェクトを作成
loop = asyncio.get_event_loop()

async def worker():
    print('start')
    await asyncio.sleep(2)
    # time.sleep(2)
    print('end')
    
if __name__ == '__main__':
    
    # #　シングルスレッド
    # worker()
    
    # #　マルチスレッド
    # t1 = threading.Thread(target=worker)
    # t2 = threading.Thread(target=worker)
    # t1.start()
    # t2.start()
    
    # #　マルチプロセス
    # p1 = multiprocessing.Process(target=worker)
    # p2 = multiprocessing.Process(target=worker)
    # p1.start()
    # p2.start() 
    
    # 非同期処理
    loop.run_until_complete(asyncio.wait([worker(),worker()]))
    loop.close()