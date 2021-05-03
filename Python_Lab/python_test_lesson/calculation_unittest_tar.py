"""
#############################################################################
unittest対象のサンプルプログラム
　・簡単な計算クラスを記述
#############################################################################
"""
class Cal(object):
    def add_num(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        return result