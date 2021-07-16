"""
#############################################################################
zeroMQ(PUSH):情報をPULLするクライアント
　→IDをPULLしてクライアントがタスクを処理する（IDを表示する）
 　※PUSHしたタスクはどれかのクライアントで1回処理されればいい
#############################################################################
"""

import zmq

context = zmq.Context()
sock = context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:5690")

while True:
    message = sock.recv()
    print("Received:{}".format(message.decode()))

