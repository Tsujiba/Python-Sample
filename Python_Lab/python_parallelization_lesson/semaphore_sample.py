"""
#############################################################################
セマフォ(semaphore):
　ロックはスレッドを１つしか実行できず、他のスレッドが待たされるが、
 　セマフォにすると、指定した数のスレッドだけ同時に実行できる
#############################################################################
"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

def worker2(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

def worker3(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')
    
if __name__ == '__main__':
    # セマフォで２つのスレッドだけ実行できる
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore, ))
    t2 = threading.Thread(target=worker2, args=(semaphore, ))
    t3 = threading.Thread(target=worker2, args=(semaphore, ))
    t1.start()
    t2.start()
    t3.start()
    print('started')
    
