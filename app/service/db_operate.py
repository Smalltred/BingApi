#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 17:58
# @Author  : Small tred
# @FileName: db_operate.py
# @Software: PyCharm
# @Blog    : https://www.hecady.com
from app import db
from app.service.service import EverydayBing
from app.models.db import Bing, Bing4k


def insert_data(table, resolution):
    # 获取数据
    data = EverydayBing("", resolution=resolution, mun=1).parse_response().get("data")[0]
    data["date"] = data["date"][0:4] + "年" + data["date"][4:6] + "月" + data["date"][6:8] + "日"
    print(data)
    if table == "bing":
        b_type = Bing
        commit_data(b_type, data)
    elif table == "bing4k":
        b_type = Bing4k
        commit_data(b_type, data)


def commit_data(b_type, data):
    db.session.add(b_type(**data))
    db.session.commit()


if __name__ == '__main__':
    insert_data(Bing, "4k")
    insert_data(Bing4k, "1080")
