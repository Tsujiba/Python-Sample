"""
#############################################################################
socket通信(socletserver側)
 -> socketclientからの通信を待ち構える
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

IP = '127.0.0.1'
PORT = 50007 


"""
TCP通信
"""
# """
# TCP通信（socket.SOCK_STREAM)のソケットを作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # socketを特定のIPアドレスとポート番号に紐づけ
    s.bind((IP, PORT))
    
    # 接続の待ち受けを開始
    s.listen(1)
    while True:
        # 接続を受信
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('data: {}, addr: {}'.format(data, addr))
                conn.sendall(b'Received:' + data)
# """ 
    
"""
UDP通信
"""
"""
# UDP通信（socket.SOCK_DGRAM)のソケットを作成
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    
    # socketを特定のIPアドレスとポート番号に紐づけ
    s.bind((IP, PORT))
    # UDPはListenする必要なし、コネクションもなし
    while True:
        data, addr = s.recvfrom(1024)
        print('data: {}, addr: {}'.format(data, addr))
"""        

