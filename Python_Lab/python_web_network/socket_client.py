"""
#############################################################################
socket通信(socletclient側)
 -> socketserverへ通信を行う
・ウェルノウンポート番号（0~1023)
・登録済みポート番号（1024~49151)
・プライベートポート番号（49152~65535)
----------------------------------------------------------------------------------------------------------
インターネットはTCP/IPと呼ぶ通信プロトコルを利用しますが、そのTCP/IPを プログラムから利用するには、
プログラムの世界とTCP/IPの世界を結ぶ特別な 出入り口が必要となります。その出入り口となるのがソケット (Socket)であり、
TCP/IPのプログラミング上の大きな特徴となっています。 このため、TCP/IP通信をソケット通信と呼ぶこともあります。
#############################################################################

"""

import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 50007 

"""
TCP通信
"""
# """
# TCP通信（socket.SOCK_STREAM)のソケットを作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # リモートソケットへ接続
    s.connect((SERVER_IP, SERVER_PORT))
    s.sendall(b'Hello!!')
    data = s.recv(1024)
    print(data)
# """
 
"""
UDP通信
"""
"""
# UDP通信（socket.SOCK_DGRAM)のソケットを作成
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # リモートソケットへ接続（コネクション）は必要なし
    s.sendto(b'Hello UDP!!',(SERVER_IP, SERVER_PORT))
""" 