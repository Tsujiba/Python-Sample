"""
#############################################################################:
・enum
　・ステータスコードを表す時につかえる
#############################################################################
"""

import enum

# サーバの状態定義（サンプル）：DBから取り出した
db = {
    'stack1': 1,
    'stack2': 2
}


# @enum.unique
# class Status(enum.Enum):
#     ACTIVE = 1
#     INACTIVE = 2
#     RUNNING = 3

# INtEnumならStatus.ACTIVEを1でも判定できる
@enum.unique
class Status(enum.IntEnum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

"""   
print(Status.ACTIVE)
print(Status.ACTIVE.name)
print(Status.ACTIVE.value)
print(repr(Status.ACTIVE))
print(Status.ACTIVE == 1)
"""

if (db['stack1'] == Status.ACTIVE):
    print('shutdown')
elif(db['stack1'] == Status.INACTIVE):
    print('terminate')
    
# UNIXのパーミッションの表現
class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1

print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W))

#RWX = Perm.R | Perm.W | Perm.X
RWX = Perm.R


if(Perm.W in RWX):
    print('OK')
else:
    print('NG:Access Denied')
    
    






