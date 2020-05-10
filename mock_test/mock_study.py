import mock
import requests
import unittest
url = "http://www.wrp.com/login"
data = {
    "username":"admin",
    "password":"123456"
}

def post_request(url,data):
    res = requests.post(url,data).json()
    return res

def get_request(url,data):
    res = requests.get(url,data).json()
    return res 


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行完毕")

    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username":"1111"
        }
        success_test = mock.Mock(return_value=data)
        post_request = success_test
        res = post_request
        self.assertEqual("11222",res())

    def test_02(self):
        url = "http://www.baidu.com"
        data = {
            "username":"admin"
        }
        success_test = mock.Mock(return_value=data)
        get_request = success_test
        res = get_request
        self.assertEqual({'username': 'admin'},res())

    def test_03(self):
        url="http://127.0.0.1:8001/get_login"   #自己搭的mock服务
        data = {
            "username":"wrp",
            "password":"123456"
        }
        res = get_request(url,data)
        print(res)

    def test_04(self):
        url="http://127.0.0.1:8001/post_login"  #自己搭的mock服务
        data = {
            "username":"wrp",
            "password":"123456"
        }
        res = post_request(url,data)
        print(res)        


if __name__=="__main__":
    unittest.main()
