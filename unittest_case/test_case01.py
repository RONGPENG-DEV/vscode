import requests
import unittest

data = {
    "username":"wrp",
    "password":"123456"
}
class TestCase01(unittest.TestCase):

    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case结束执行")

    @classmethod
    def setUpClass(cls):
        print("case类开始执行")

    @classmethod
    def tearDownClass(cls):
        print("case类结束执行")

    def test_01(self):
        data1 = {
            "username":"wrp",
            "password":"12345"
        }
        self.assertDictEqual(data,data1,msg="dict结果不相等")
    def test_02(self):
        data1 = {
            "username":"wrp",
            "password":"123456"
        }
        self.assertDictEqual(data,data1,msg="dict结果不相等")
    def test_03(self):
        flag = True
        self.assertFalse(flag,msg="结果不为false")
    def test_04(self):
        flag = False
        self.assertTrue(flag,msg="结果不为true")
    def test_05(self):
        flag = "111"
        flag1 = "111"
        self.assertEqual(flag,flag1,msg="字符串不相等")
    def test_07(self):
        flag = "asdfsdghghdgfsd"
        s = "h"
        self.assertIn(s,flag,msg="字符未在字符串中")
    



if __name__ == "__main__":
    unittest.main() 