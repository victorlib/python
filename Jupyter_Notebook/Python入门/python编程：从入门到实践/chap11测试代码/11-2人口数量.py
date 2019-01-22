import unittest
from chap11测试代码.city_function import *


class CityTestCase(unittest.TestCase):
    """测试city_function.py"""

    def test_city_country(self):
        """能够正确处理像Santiago, Chile这样的地名吗"""
        t = place('santiago', 'chile')
        self.assertEqual(t, 'Santiago, Chile')

    def test_city_country_population(self):
        t = place2('santiago', 'chile', population=5000000)
        self.assertEqual(t, 'Santiago, Chile - population 5000000')


unittest.main()

