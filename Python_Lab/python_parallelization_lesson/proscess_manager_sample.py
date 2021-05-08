"""
#############################################################################
プロセスのマネージャー:
　・個別でメモリ管理をしているプロセス間で共有メモリを実現する
 Value、ArrayよりもPython的な記述方法で書きやすいが、
 速度が遅いという問題がある
#############################################################################
"""
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(list, dict, nspace):
    list.reverse()
    dict['x'] += 1
    nspace.y += 1
            
if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        list = manager.list()
        dict = manager.dict()
        nspace = manager.Namespace()
        
        list.append(1)        
        list.append(2)
        list.append(3)
        dict['x'] = 0
        nspace.y = 0
        
        p1 = multiprocessing.Process(target=worker1, args=(list, dict, nspace))
        p2 = multiprocessing.Process(target=worker1, args=(list, dict, nspace))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        logging.debug(list)
        logging.debug(dict)
        logging.debug(nspace)
        
        
        