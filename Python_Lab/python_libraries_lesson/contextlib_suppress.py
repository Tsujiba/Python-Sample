"""
#############################################################################:
・contextlib.suppress
　　→エラーを抑圧する
#############################################################################
"""

import contextlib
import os

try:
    os.remove('tmpfile.txt')
except FileNotFoundError:
    pass

#　上記を下のように記述できる（try~,exceptでpassするものを簡単に記述する、コマンド実行など）
with contextlib.suppress(FileNotFoundError):
    os.remove('tmpfile2.txt')
    
    





