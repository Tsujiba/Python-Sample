"""
#############################################################################
プロセスのプールとブロック:
　・プロセスをプール化して、非同期で並列にはしらせることができる
#############################################################################
"""
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i
        
if __name__ == '__main__':
    # プールできるプロセス数を３に指定してプール作成
    with multiprocessing.Pool(3) as p:
        
        """
        # 利用法１
        # ブロックしてworkerプロセスを実行（同期）
        logging.debug(p.apply(worker1, (200, )))
        logging.debug('executed apply')
        # workerプロセスを非同期で実行
        p1 = p.apply_async(worker1, (100,))
        p2 = p.apply_async(worker1, (150,))
        logging.debug(p1.get())
        logging.debug(p2.get())
        # logging.debug(p2.get(timeout=1))
        """
        
        # 利用法2(mapを利用する)
        # map（同期）
        """
        result = p.map(worker1, [100, 200])
        logging.debug('executed')
        logging.debug(result)
        """
        
        #map(非同期)
        result = p.map_async(worker1, [100, 200])
        logging.debug('executed')
        logging.debug(result.get())