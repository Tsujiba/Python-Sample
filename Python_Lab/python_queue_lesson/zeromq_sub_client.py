"""
#############################################################################
zeroMQ(PUSH):情報をSUBSCRIBEするクライアント
　→IDをSUBSCRIBEしてクライアントがタスクを処理する（IDを表示する）
 　※リアルタイムに処理する
#############################################################################
"""

import zmq

context = zmq.Context()
sock = context.socket(zmq.SUB)
sock.setsockopt(zmq.SUBSCRIBE, b'sub1:')
sock.connect("tcp://127.0.0.1:5690")

while True:
    message = sock.recv()
    print("Received:{}".format(message.decode()))

