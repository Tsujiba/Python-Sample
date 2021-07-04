"""
#############################################################################:
・formatの色々な使い方
　・{（値）:（設定）}→コロンで区切った右側に色々な設定できる
#############################################################################
"""

print('{}{}{}'.format(1, 2, 3))
print('{0}{1}{2}'.format(1, 2, 3))
print('{2}{1}{0}'.format(1, 2, 3))
print('{name}、{old}、{height}cm'.format(name='yu', old=26, height=183))

print('{:<30}'.format('left'))
print('{:>30}'.format('right'))
print('{:^30}'.format('center'))

print('{:*<30}'.format('left'))
print('{name:{fill}{align}{width}}'.format(name='center', fill='*', align='^', width=30))


print('{:,}'.format(123456789))
print('{:+f}{:+f}'.format(3.14, -3.14))
print('{:.2%}'.format(19/22))






