"""
#############################################################################
multiprocessing:マルチプロセスでプログラムを実行する
 　・複数のコアでプログラムを実行
  　　→スレッドとほとんど書き方は同じ
#############################################################################
"""
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(5)
    logging.debug('end')
    
def worker2(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(2)
    logging.debug('end')
    
if __name__ == '__main__':
    i = 1
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    # プロセスのデーモン化（t2スレッドが終了した時にプログラムが終了する）
    t1.daemon = True
    t2 = multiprocessing.Process(target=worker2, args=(i, ))
    t1.start()
    t2.start()
    # デーモンプロセス終了まで待機することを明示的に指定
    t1.join()
    print('started')
    
