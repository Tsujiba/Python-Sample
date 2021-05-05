"""
#############################################################################
salary：mockでのテスト対象のプログラム
　・連携先のシステム'http://localhost/host'が利用できないときにテストを行いたい
 　　→mockを利用する（test_salary_sanple.py)
#############################################################################

"""

import requests

class ThirdPartyBonusRestApi(object):
    # ボーナス額を返すシステムから値を取り出す関数
    def bonus_price(self, year):
        r = requests.get('http://localhost/host', params={'year': year})
        # JSON形式で{'price': 1}などで帰ってくるvalueをリターン
        return r.json()['price']
    
class Salary(object):
    def __init__(self, base=100, year=2021):
        self.bonus_api = ThirdPartyBonusRestApi()
        self.base = base
        self.year = year
    
    def calculation_salary(self):
        bonus = 0
        try:
            bonus = self.bonus_api.bonus_price(year=self.year)
        except ConnectionRefusedError:
            bonus = 0    
        return self.base + bonus
    
