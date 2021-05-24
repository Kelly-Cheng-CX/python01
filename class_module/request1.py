import requests

# 登录

url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobilephone": "18111111111", "pwd": "123456"}
res = requests.post(url, data)
print(res.json())


# # 充值
# session = requests.Session()
# session 会自动将cookie带上

# recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# recharge_data = {"mobilephone": "18111111111", "amount": "1000"}
# res = session.post(recharge_url, data=recharge_data)
# print(res.text)
# session.close()
#
