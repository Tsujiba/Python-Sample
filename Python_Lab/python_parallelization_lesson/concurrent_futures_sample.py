"""
#############################################################################
高水準のインターフェース:concurrent.futures
　簡単にマルチスレッド、プロセスを実行できる
 　単純な並列化ならこちらを利用してもよいかも
#############################################################################
"""
import logging
import time
import concurrent.futures

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')
# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s')



def worker(x, y):
    logging.debug('start')
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r
    
         
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # f1 = executor.submit(worker, 2, 4)
        # f2 = executor.submit(worker, 3, 5)
        # logging.debug(f1.result())
        # logging.debug(f2.result())
       
       args = [[2,3], [4, 5]]
       r = executor.map(worker, *args)
       logging.debug(r)
       logging.debug([i for i in r])
       
if __name__ == '__main__':
    main()
    