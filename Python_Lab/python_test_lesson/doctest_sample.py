"""
#############################################################################
doctest：ドキュメントの中にテストを記述できる
　・全てのテストを記述すると長くなるので、他のプログラマに見せるために
 　　利用するなど
#############################################################################

"""

class Call(object):
    def add_num(self, x, y):
        """Add num
        ここにテストを記述できる
        >>> c = Call()
        >>> c.add_num(1, 1)
        2
        
        >>> c.add_num('1', '1')
        Traceback (most recent call last):
        ....
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        return result
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    