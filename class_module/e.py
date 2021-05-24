import requests

# 登录

# url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# data = {"mobilephone": "18111111111", "pwd": "123456"}
# headers = {"X-Lemonban-Media-Type": "lemonban.v2"}

class we:
    def visit(url, data,headers):
        res = requests.post(url, data,headers=headers)
        return res.json()


# assert 1 + 2 == 2
# print("assert finished")

# print(login(login_url, data, headers))

# # 充值
# session = requests.Session()
# session 会自动将cookie带上

# recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# recharge_data = {"mobilephone": "18111111111", "amount": "1000"}
# res = session.post(recharge_url, data=recharge_data)
# print(res.text)
# session.close()
#
