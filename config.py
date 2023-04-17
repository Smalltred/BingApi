#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 1:17
# @Author  : Small tred
# @FileName: config.py
# @Software: PyCharm
# @Blog    : https://www.hecady.com


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345678@127.0.0.1:3306/bing?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_ECHO = True
    DEBUG = True
    JSON_AS_ASCII = False
