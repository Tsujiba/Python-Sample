"""
#############################################################################
unittest：unittestプログラム
　・calculation_unittest_tar.pyをテストする
#############################################################################
"""

import unittest

import calculation_unittest_tar

class Caltest(unittest.TestCase):
    
    release_name = 'lesson2'
    
    # テスト実行前のセットアップ(開始前処理)
    def setUp(self):
        print('setUp!')
        self.cal = calculation_unittest_tar.Cal()
        
    # テスト実行後のティアダウン(開始後処理)
    def tearDown(self):
        print('clean up!')
        del self.cal

    # @unittest.skip('skip!')
    @unittest.skipIf(release_name=='lesson', 'skip!!')
    # プレフィックスを必ずtest_にする
    def test_add_num(self):
        # cal = calculation_unittest_tar.Cal()
        self.assertEqual(self.cal.add_num(1,1), 2)
        
    # 例外処理のテスト
    def test_add_num_raise(self):
        # cal = calculation_unittest_tar.Cal()
        with self.assertRaises(ValueError):
            self.cal.add_num('1', '1')
    
if __name__ == '__main__':
    unittest.main()
