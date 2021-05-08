"""
#############################################################################
バリア(barrier):
　・バリアは複数のスレッドが同時に立ち上げったときサービスを実行できる
　　→クライアントとサーバのスレッドが立ち上がったときにサービスを行うなど
#############################################################################
"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(barrier):
    r = barrier.wait()
    logging.debug('NUM={}'.format(r))
    while True: 
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker2(barrier):
    r = barrier.wait()
    logging.debug('NUM={}'.format(r))
    while True: 
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

# def worker3(barrier):
#     with barrier:
#         logging.debug('start')
#         time.sleep(3)
#         logging.debug('end')
#         barrier.notifyAll()
        
if __name__ == '__main__':
    # 2つのスレッドが立ち上がったときサービスを開始を指定する
    barrier = threading.Barrier(2)
    t1 = threading.Thread(target=worker1, args=(barrier, ))
    t2 = threading.Thread(target=worker2, args=(barrier, ))
    #t3 = threading.Thread(target=worker3, args=(barrier, ))
    t1.start()
    t2.start()
    #t3.start()
    print('started')
    
