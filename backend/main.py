from sqlite3 import Cursor
from threading import local
from typing import Optional
from fastapi import FastAPI

import json
import mysql.connector
import datetime


app = FastAPI()


# 本地数据库配置
localdb = {
    "user": "admin",
    "password": "123698745leo",
    "host": "127.0.0.1",
    "database": "temp"
}



'''
查询用户数据接口
'''
@app.get("/userinfo")
def get_userinfo():
    cnx = mysql.connector.connect(user = localdb["user"],
                                  password = localdb["password"],
                                  host = localdb["host"], 
                                  database = localdb["database"])
    # 查询游针
    cursor = cnx.cursor()

    query_sql = "select user_id, user_name, user_num, car_name, car_start_time, car_end_time " + \
                "from user, car where user.user_num = car.for_user_num;"

    cursor.execute(query_sql)

    # 存储数据的列表
    res_list = []

    # 全部数据
    data = cursor.fetchall()
    # 数据描述
    desc = cursor.description

    res_disc = {}
    # 将数据向字典进行转换
    for i in range(0, len(data)):
        res_disc = {}
        for j in range(0, len(data[0])):
            # 将时间str化
            if desc[j][0] == "car_start_time" or desc[j][0] == "car_end_time":
                res_disc[desc[j][0]] = str(data[i][j])
                continue
            res_disc[desc[j][0]] = data[i][j]
        res_list.append(res_disc)

    # print(json.dumps(res_list))

    # 关闭连接
    cursor.close()
    cnx.close()

    return json.dumps(res_list)
    # return json.dumps({"status": "successful"})


'''
查询保安数据接口
'''
@app.get("/guardinfo")
def get_guardinfo():
    return json.dumps({"status": "successful"})











    