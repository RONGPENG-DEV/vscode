import unittest
import sys
import os
import unittest
base_path = os.getcwd()
sys.path.append(base_path)
from Base.base_request import request

data = {
    "username":"wrp",
    "password":"123456"
}

url = "http://www.baiu.com"
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

    @unittest.skipIf(url!="http://www.baidu.com","这个case不执行")
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
    def test_06(self):
        res = request.run_main('get',url,data)
        print(res)



if __name__ == "__main__":
    #unittest.main() 
    suite = unittest.TestSuite()
    #suite.addTest() #批量添加
    
    #单条添加，让用例按自定顺序执行
    # suite.addTest(TestCase01('test_06'))
    # suite.addTest(TestCase01('test_04'))
    # suite.addTest(TestCase01('test_02'))
    # suite.addTest(TestCase01('test_05'))
    # suite.addTest(TestCase01('test_01'))
    # suite.addTest(TestCase01('test_03'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    

    #使用list添加用例
    tests = [TestCase01('test_06')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)