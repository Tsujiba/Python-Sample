from fabric.api import run, env
from fabric.decorators import roles, task

env.hosts = ['root@172.16.200.101:22', 'root@172.16.200.102:22']
env.passwords = {
    'root@172.16.200.101:22': 'root',
    'root@172.16.200.102:22': 'root',
}
env.roledefs = {
    'web': ['root@172.16.200.101:22'],
    'db':['root@172.16.200.102:22']
}

@roles('web')
def host_type():
    run('uname -s')

@roles('db')    
def hsot_files():
    run('ls -al')

# taskでデコレータしたものはfab --list ででてくる
@task
def go():
    run('ls -al')    
