"""
#############################################################################:
・contextlib.redirect_stdout_err
　 →標準出力、標準出力エラーをリダイレクトする
#############################################################################
"""

import contextlib
import logging


with open('stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        # この中に記述は全てファイルにリダイレクトされる
        print('redirect test!!')




        
         
