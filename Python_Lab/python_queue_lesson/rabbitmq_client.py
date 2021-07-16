import tasks

# result =tasks.build_server.delay()
# result =tasks.build_server() # 普通に実行する場合

# result =tasks.build_servers.delay()
# result =tasks.build_server_with_cleanup.delay()
result =tasks.deploy_customer_server.delay()

print('doing...')
print(result)
