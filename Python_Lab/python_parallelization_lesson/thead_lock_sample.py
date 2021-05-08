"""
#############################################################################
Lock:マルチスレッドでプログラムを実行する際に２つのスレッドで同じデータの更新する際
　　　データの不整合を防ぐ
#############################################################################
"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(data, lock):
    logging.debug('start')
    # ロックを要求する(withステートメント記述版)
    with lock:
        i = data['count']
        time.sleep(5)
        data['count'] = i + 1
        logging.debug(data)
    logging.debug('end')

def worker2(data, lock):
    logging.debug('start')
    # ロックを要求する
    lock.acquire()
    i = data['count']
    data['count'] = i + 1
    logging.debug(data)
    # ロックを開放する
    lock.release()
    logging.debug('end')
    
if __name__ == '__main__':
    common_data = {'count':0}
    lock = threading.Lock()
    t1 = threading.Thread(target=worker1, args=(common_data, lock))
    t2 = threading.Thread(target=worker2, args=(common_data, lock))
    t1.start()
    t2.start()
    # デーモンスレッド終了まで待機することを明示的に指定
    t1.join()
    print('started')
    
