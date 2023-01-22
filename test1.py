import unittest
from unittest import TestCase
from main import task1, task2, task3


class Test1(TestCase):
    def test1(self):
        res = task1()
        self.assertNotIsInstance(res, dict)
        self.assertListEqual(res,[{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])
  
class Test2(TestCase):  
    def test2(self):
        res = task2()
        self.assertIsInstance(res, set)
        self.assertSetEqual(res,{98, 35, 213, 54, 119, 15})

class Test3(TestCase):
    def test3(self):
        res = task3()
        self.assertIsInstance(res, str)
        self.assertEqual(res,"yandex")

if __name__ == '__main__':
    unittest.main()