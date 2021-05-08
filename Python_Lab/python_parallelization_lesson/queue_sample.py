"""
#############################################################################
キュー(Queus):
　・キューはリスト形式でデータを出し入れする（FIFO）
  ・putでいれて、getで取り出す
  ・getはキューに値が入ってくるまで永遠に待ち続ける
#############################################################################
"""
import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(queue):
    logging.debug('start')
    queue.put(100) # [100,]
    time.sleep(5)
    queue.put(200)
    time.sleep(3)
    logging.debug('end')

def worker2(queue):
    logging.debug('start')
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end')
    
if __name__ == '__main__':
    # キューを用意する
    queue = queue.Queue()
    t1 = threading.Thread(target=worker1, args=(queue, ))
    t2 = threading.Thread(target=worker2, args=(queue, ))
    t1.start()
    t2.start()
    print('started')
    
