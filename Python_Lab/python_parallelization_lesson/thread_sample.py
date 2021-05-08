"""
#############################################################################
thread:マルチスレッドでプログラムを実行する
スレッド→ユーザスレッド→ユーザが生成するスレッド
　　　　　デーモンスレッド：デーモンスレッド以外のスレッドが終了したときに
     　　　　　　　　　　　　プログラムが終了するのを妨げないスレッド
#############################################################################
"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    
def worker2(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(2)
    logging.debug('end')
    
if __name__ == '__main__':
    t1 = threading.Thread(name='rename_worker1', target=worker1)
    # スレッドのデーモン化（t2スレッドが終了した時にプログラムが終了する）
    t1.setDaemon(True)
    #t2 = threading.Thread(target=worker2, args=(20, ), kwargs={'y': 50})
    # タイマーで3秒後にt2を実行する
    t2 = threading.Timer(3, worker2, args=(20, ), kwargs={'y': 50})
    t1.start()
    t2.start()
    # デーモンスレッド終了まで待機することを明示的に指定
    t1.join()
    print('started')
    
