import unittest
from unittest import TestCase
import requests
from yadisk1 import Yandex 


class Test_yadisk(TestCase):
    @unittest.expectedFailure
    def test1(self):
        response = Yandex()
        self.assertIsInstance(response, int)
        self.assertEqual(response, 201)

    @unittest.expectedFailure
    def test2(self):
        Yandex()
        response = Yandex()
        self.assertEqual(response, 200)

    @unittest.expectedFailure
    def test3(self):
        Yandex()
        token = '' # тут токен
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        response = requests.get(f'{URL}?path=Folder', headers=headers)
        self.assertEqual(response, 404)    

if __name__ == '__main__':
    unittest.main()