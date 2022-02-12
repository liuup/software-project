from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import json
import mysql.connector


app = FastAPI()


# 暂时允许所有源访问fastapi
origins = {
    "*"
}


# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 本地数据库配置
localdb = {
    "user": "admin",
    "password": "123698745leo",
    "host": "127.0.0.1",
    "database": "temp"
}


success_json = json.dumps({"status": "successful"})
failure_json = json.dumps({"status": "failure"})


'''
查询用户数据接口, 获取已通过和未通过的用户数据
'''
@app.get("/user/info/{ispass}")
def get_userinfo(ispass: int):
    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()

    query_sql = "select user_id, user_name, user_num, car_name, car_start_time, car_end_time " + \
                "from user, car where user.user_num = car.for_user_num and car.car_is_pass = " + str(ispass)

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

    # 关闭连接
    cursor.close()
    cnx.close()

    if len(res_list) == 0:
        return failure_json
    else:
        return json.dumps(res_list)
    


# FIXME:
'''
查询保安数据接口
'''
@app.get("/guard/info")
def get_guardinfo():
    return success_json



'''
用户登录接口
'''
class User(BaseModel):
    user_num: str
    user_pwd: str

@app.post("/user/login")
def userlogin(user: User):
    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()

    # 将接收到的数据转为字典
    post_dict = json.loads(user.json())

    # query_sql = "select * from user where user_num = " + post_dict["user_num"] + \
    #             " and user_pwd = " + post_dict["user_pwd"]

    query_sql = "select * from user where user_num = {} and user_pwd = {}".format(post_dict["user_num"], post_dict["user_pwd"])

    cursor.execute(query_sql)

    # 全部数据
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    # 查询失败
    if len(data) == 0:
        return failure_json

    # 查询成功
    if post_dict["user_num"] == data[0][2] and post_dict["user_pwd"] == data[0][3]:
        return success_json



'''
保安登录接口
'''
class Guard(BaseModel):
    guard_num: str
    guard_pwd: str

@app.post("/guard/login")
def guardlogin(guard: Guard):
    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()

    # 将请求体转为字典
    post_dict = json.loads(guard.json())

    query_sql = "select * from guard where guard_num = {} and guard_pwd = {}".format(post_dict["guard_num"], post_dict["guard_pwd"])

    cursor.execute(query_sql)

    # 全部数据
    data = cursor.fetchall()

    cursor.close()
    cnx.close()

    # 查询失败
    if len(data) == 0:
        return failure_json

    # 查询成功
    if post_dict["guard_num"] == data[0][2] and post_dict["guard_pwd"] == data[0][3]:
        return success_json



'''
用户注册接口
'''
@app.post("/user/register")
def user_register():
    return success_json


# FIXME:
'''
保安注册接口
'''
@app.post("/guard/register")
def guard_register():
    return success_json



'''
修改车辆通过接口
'''
class Car(BaseModel):
    for_user_num: str
    car_name: str
    car_is_pass: str

@app.post("/car/manage")
def car_manage(car: Car):
    print(car)

    cnx = mysql.connector.connect(**localdb)
    # 查询游针
    cursor = cnx.cursor()
    
    # 获取post请求体的字典类型数据
    car_dict = json.loads(car.json())
      
    sql = "update car set car_is_pass = '{}' where for_user_num = '{}' and car_name = '{}';"\
                .format(str(car_dict["car_is_pass"]), str(car_dict["for_user_num"]), str(car_dict["car_name"]))

    # print(query_sql)
    cursor.execute(sql)
    
    cnx.commit()

    cursor.close()
    cnx.close()

    if cursor.rowcount == 0:
        return failure_json
    else:
        return success_json