#coding = utf08
import requests
import json
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_json import get_value
from Util.handle_ini import handle_ini

class BaseRequest:
    def send_post(self,url,data):
        res = requests.post(url=url, data=data).text
        return res

    def send_get(self,url,data):
        res = requests.get(url=url,params=data).text
        return res

        

    def run_main(self,method,url,data):
        """
        执行方法，传递method,url,data参数
        """
        return get_value("api1")
        base_url = handle_ini.get_value('host')
        if 'http' in base_url:
            if url != None:
                url = base_url+url
                print(url)
            else:
                url = base_url
        if method == 'get':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res


request = BaseRequest()


if __name__=="__main__":
    request = BaseRequest()
    request.run_main('get','',"{'username':'11111'}")