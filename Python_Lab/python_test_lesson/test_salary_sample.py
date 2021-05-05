"""
#############################################################################
test_salary：mockを利用したテストプログラム
　・連携先のシステム'http://localhost/host'が利用できないときにテストを行いたい
 　　→mockを利用する（対象PGtest_salary_sanple.py)
#############################################################################
"""

import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary_sample


class TestSalarySample(unittest.TestCase):
    def test_calulation_salary(self):
        s = salary_sample.Salary(year=2021)
        # MagicMockでボーナス額１がリターンされたことにする
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)

        # bonus_api.bonus_priceが呼ばれているか確認
        s.bonus_api.bonus_price.assert_called()
        # bonus_api.bonus_priceが1度だけ呼ばれているか確認
        s.bonus_api.bonus_price.assert_called_once()
        # bonus_api.bonus_priceのパラメータが正しく設定されて呼ばれているか確認
        s.bonus_api.bonus_price.assert_called_with(year=2021)

    # 'salary_sample.ThirdPartyBonusRestApi.bonus_price'はモックとデコレータで宣言
    @mock.patch('salary_sample.ThirdPartyBonusRestApi.bonus_price')
    def test_calulation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1
        s = salary_sample.Salary(year=2021)
        # MagicMockでボーナス額１がリターンされたことにする
        self.assertEqual(s.calculation_salary(), 101)
        
    # 上記をwithステートメントで記述（モックを利用する範囲を指定したいときなど）
    def test_calulation_salary_patch_with(self):
        with mock.patch('salary_sample.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1
            s = salary_sample.Salary(year=2021)
            # MagicMockでボーナス額１がリターンされたことにする
            self.assertEqual(s.calculation_salary(), 101)

    # 上記をpatcherで記述(setUPとtearDownでpatcher(モック開始、終了時点を宣言))
    def setUp(self):
        self.patcher = mock.patch('salary_sample.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()
        
    def tearDown(self):
        self.patcher.stop()
        
    def test_calulation_salary_patch_patcher(self):
        self.mock_bonus.return_value = 1
        s = salary_sample.Salary(year=2021)
        # MagicMockでボーナス額１がリターンされたことにする
        self.assertEqual(s.calculation_salary(), 101)

    # sideeffectでモックの返り値を関数化したり、エクセプションを入れたり、リスト化が可能
    def test_calulation_salary_patch_side_effect(self):
        
        # def f(year):
        #    return year * 2
        
        self.mock_bonus.side_effect = ConnectionRefusedError
        s = salary_sample.Salary(year=2021)
        salary_price = s.calculation_salary()
        # MagicMockでボーナス額１がリターンされたことにする
        self.assertEqual(salary_price, 100)
        
        # class全体をモックもできる（デコレータでspec=Trueとする)


if __name__ == '__main__':
    unittest.main()
