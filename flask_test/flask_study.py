#encoding = 'utf-8'
from flask import Flask
import json
from flask import request
app = Flask(__name__)

@app.route('/')
def login():
    data= json.dumps({
        "username":"wrp",
        "password":"111111"
    })
    return data

@app.route('/passport/user/login',methods=['GET'])
def login1():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:
        data= json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登陆成功",
            "info":"www.baidu.com"
        })
    else:
        data = json.dumps({
            "message":"请传递参数"
        })

    return data


@app.route('/passport/user/post_login',methods=['POST'])
def post_login():
    request_method = request.method
    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        data= json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登陆成功",
            "info":"www.baidu.com"
        })
        
    else:
        data = json.dumps({
            "message":"请求不合法"
        })
    return data


if __name__ == "__main__":
    app.run()
