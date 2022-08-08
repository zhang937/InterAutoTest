import urllib3
import os
from locust import HttpUser, TaskSet, task,HttpLocust
from urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
urllib3.disable_warnings(InsecureRequestWarning)
"""
SequentialTaskSet",
"wait_time",
"task",
"tag",
"TaskSet",
"HttpUser",===HttpLocust
"FastHttpUser",
"User",
"between",
"constant",
"constant_pacing",
"constant_throughput",
"events",
"LoadTestShape",
"""



class MyBlogs(TaskSet):
    @task(1)
    def get_blog(self):

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        req=self.client.get("/imyalost", headers=header, verify=False,name="打开首页")
        if req.status_code == 200:
            print("success")
        else:
            print("fail")
    @task(1)
    def get_post(self):
        url="/login"
        data={}
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

        with  self.client.post(url, data=data, headers=headers, verify=False, name="登录") as req:
        # req=self.client.post(url,data=data,headers=headers,verify=False,name="登录")
            if req.status_code == 200:
                print("success")
                return req.text
            else:
                print("fail")

class websitUser(HttpUser):
    tasks= [MyBlogs]
    min_wait = 3000
    max_wait = 6000
    host = "https://www.cnblogs.com"
    # 参数化数据存储用csv,json，yaml,xml等。
    from random import choice # 在列表中随机取值



if __name__ == "__main__":
    os.system("locust -f Locustdemo.py ") # 单进程
    os.system("locust -f Locustdemo.py --slave")  # master与slave 在同一个节点
    os.system("locust -f Locustdemo.py --slave  --master --host='192.20.1.102'") #master与slave 不在同一个节点 需要指定master 主机


     # 进程 一个CPU启动一个进程。