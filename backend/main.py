from sqlite3 import Cursor
from typing import Optional
from fastapi import FastAPI

import json
import mysql.connector

app = FastAPI()

mysql = {
    "user": "admin",
    "password": "123698745leo",
    "host": "127.0.0.1",
    "database": "temp"
}


@app.get("/userinfo")
def get_userinfo():
    cnx = mysql.connector.connect(mysql["user"],
                                  mysql["password"],
                                  mysql["host"], 
                                  mysql["database"])
    cursor = cnx.cursor()

    query_sql = "select * from user, car where user.user_num = car.user_num"

    cursor.execute(query_sql)

    for data in cursor:
        print(data)


    # 关闭连接
    cursor.close()
    cnx.close()


    return json.dumps({"status": "successful"})



