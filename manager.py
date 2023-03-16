#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 17:15
# @Author  : Small tred
# @FileName: manager.py
# @Software: PyCharm
# @Blog    : https://www.hecady.com
from flask_script import Manager
from app import create_app
from app.service.db_operate import insert_data

app = create_app()

manager = Manager(app)


@manager.command
def init_db():
    with app.app_context():
        from app.models.db import db
        db.create_all()


@manager.command
def drop_db():
    with app.app_context():
        insert_data("bing", "4k")
        insert_data("bing4k", "4k")


if __name__ == '__main__':
    manager.run()
