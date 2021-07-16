"""
#############################################################################
RabbitMQ:ブレーカーありのキューイングシステム（RabitMQサーバを動かしておく）
　→CeleryというRabitMQを扱うことができるPythonライブラリをいれる
#############################################################################
"""

import re
import time
import random

import celery

app = celery.Celery(
    'tasks',
    broker='amqp://guest@localhost',
    backend='amqp://guest@localhost'
)

@app.task
def build_server():
    print('building... wait 5 sec..')
    time.sleep(5)
    server_id = random.randint(1, 100)
    return server_id

# 上を10回実行する（グループ機能）
@app.task
def build_servers():
    group = celery.group(
        build_server.s() for _ in range(10)
    )
    return group()

# コールバック関数
@app.task
def callback(result):
    for server_id in result:
        print(server_id)
        print('clean up!!!')
        return 'done'
    
# 10回サーバを立ち上げタスクを実行後にコールバック関数を呼び出す
@app.task
def build_server_with_cleanup():
    c = celery.chord(
        (build_server.s() for _ in range(10)),
        callback.s()
    )
    return c()

# DNS設定タスク
@app.task
def setup_dns(server_id):
    print('set up dns for {}'.format(server_id))
    return 'done for {}'.format(server_id)

# サーバをデプロイ後にチェインでDNS設定を行うタスク
@app.task
def deploy_customer_server():
    chain = build_server.s() | setup_dns.s()
    return chain()
