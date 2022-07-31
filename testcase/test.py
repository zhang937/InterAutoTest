import requests
from utils.RequestsUtil import Request
from utils.YamlUtil import YamlReader
from config.Conf import ConfigYaml
"""
淘宝京东
5个接口：登陆,个人信息,商品列表,购物车,订单
接口请求验证：status_code ,code 响应json 校验,数据库校验
get post delete pull
"""

# url="http://www.baidu.com"
#
# headers={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
# }
# r=Request()
# t=r.get(url,headers=headers)
# r.log.debug(t)

# import yaml
# with open("data_demo.yml",'r') as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)

# aa=YamlReader("../config/conf.yml").data()
# print(aa)

import pytest
print(pytest.__version__)