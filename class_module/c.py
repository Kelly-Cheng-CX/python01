import requests
from flask import Flask

app = Flask(__name__)

"""

"""

"""
/login地址和login函数绑定在了一起
访问/login地址 ， 函数会自己调用
"""


@app.route("/login", methods=['GET', 'POST'])  # 接口地址，@装饰器
def login():
    return {"msg": "已经111111发了"}


if __name__ == '__main__':
    app.run()



