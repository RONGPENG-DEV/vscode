import unittest
import sys
import os
import unittest
import mock
import json
import HTMLTestRunner
base_path = os.getcwd()
sys.path.append(base_path)
from Base.base_request import request



def read_json():
    with open(base_path+"/Config/user_data.json") as f:
        data =json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]

host = "http://www.imooc.com/"
class ImoocCase(unittest.TestCase):
    def test_banner(self):
        url = host  +'api1'
        data = {
            "username":"wrp",
            "password":"123456"
        }
        # mock_method = mock.Mock(return_value=read_json())
        mock_method = mock.Mock(return_value=get_value("api1"))
        request.run_main = mock_method
        res = request.run_main('post',url,data)
        self.assertEqual(res['errorCode'],1006)

    def test_banner1(self):
        url = host  +'api2'
        data = {
            "username":"wrp",
            "password":"123456"
        }
        # mock_method = mock.Mock(return_value=read_json())
        mock_method = mock.Mock(return_value=get_value("api1"))
        request.run_main = mock_method
        res = request.run_main('post',url,data)
        self.assertEqual(res['errorCode'],1016)

        
if __name__=="__main__":
    suite = unittest.TestSuite()
    tests = [ImoocCase('test_banner'),ImoocCase('test_banner1')]
    suite.addTests(tests)
    file_path = base_path+'/report/report.html'
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is a test", description="WRP Test")
        runner.run(suite)
    f.close()
    # unittest.main()