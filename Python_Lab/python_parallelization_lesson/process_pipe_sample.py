"""
#############################################################################
パイプ:プロセス間でデータの受け渡しができる
　・プロセスをスレッドと違い、メモリを共有しておらず、独自のメモリ管理を行うため
 　　データの受け渡し方にキューまたはパイプを利用する
#############################################################################
"""
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def f(conn):
    conn.send(['test'])
    time.sleep(3)
    conn.close()
        
if __name__ == '__main__':
    # パイプするペアのコネクションを作成する
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    logging.debug(child_conn.recv())
