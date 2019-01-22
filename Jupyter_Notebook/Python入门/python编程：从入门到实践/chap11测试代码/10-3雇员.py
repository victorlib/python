import unittest
from chap11测试代码.Employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('zhang', 'san', 100000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 101000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 110000)


unittest.main()
