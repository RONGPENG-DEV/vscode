import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import HandExcel
from Base.base_request import request
#['imooc_001', '登陆', 'yes', None, 'login', 'post', '{"username":"111111","password":"123456"}']
class RunMain:
    def run_case(self):
        filename = "test.xlsx"
        he = HandExcel(filename)
        rows = he.get_rows()
        for i in range(rows):
            data = he.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[5]
                url = data[4]
                data1 = data[6]
                res = request.run_main(method,url,data1)
                print(res)

if __name__ == "__main__":
    run = RunMain()
    run.run_case()


