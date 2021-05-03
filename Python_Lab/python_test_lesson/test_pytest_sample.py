"""
#############################################################################
pytest：unittestプログラム
　・calculation_unittest_tar.pyをテストする
  ・unittestよりも機能が充実している
  pytest ~/test_pytest_sample.pyで実行できる
  他参考：vscodeでのpytestテスト
  https://code.visualstudio.com/docs/python/testing
　※test_とファイル名に記述する必要がある
#############################################################################
"""

import pytest

import calculation_unittest_tar

# クラスの接頭辞にTestがいる、メソッドもtest_から始める
class TestCal(object):
    is_release = True 
    
    # テスト実行前のセットアップ(開始前処理)
    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        self.cal = calculation_unittest_tar.Cal()
        
    # テスト実行後のティアダウン(開始後処理)
    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        del self.cal

    # @pytest.mark.skip(reason='skip!')
    # @pytest.mark.skipIf(is_release==False, reason='skip!')
    # 正常系テスト
    def test_add_num(self):
        assert self.cal.add_num(1, 1) == 2
        
    # 例外処理のテスト
    def test_add_num_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num('1', '1')