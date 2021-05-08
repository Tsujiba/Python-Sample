"""
#############################################################################
イベント(event):
　・イベントは各スレッドの順序性を制御できる
  ・event.wait()で他のスレッドがevent.set()を呼び出すまで待機する
　　→worker1,2は同時に実行
#############################################################################
"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(event):
    event.wait()
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')

def worker2(event):
    event.wait()
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')

def worker3(event):
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')
    event.set()
    
if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=worker1, args=(event, ))
    t2 = threading.Thread(target=worker2, args=(event, ))
    t3 = threading.Thread(target=worker3, args=(event, ))
    t1.start()
    t2.start()
    t3.start()
    print('started')
    
