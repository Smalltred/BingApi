#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 17:06
# @Author  : Small tred
# @FileName: db.py.py
# @Software: PyCharm
# @Blog    : https://www.hecady.com
from app import db


class Bing(db.Model):
    __tablename__ = 'bing'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='ID')
    title = db.Column(db.String(255), unique=True, nullable=True, comment='标题')
    location = db.Column(db.String(255), unique=True, nullable=True, comment='地点')
    url = db.Column(db.String(255), unique=True, nullable=True, comment='图片地址')
    date = db.Column(db.String(255), unique=True, nullable=True, comment='日期')


class Bing4k(db.Model):
    __tablename__ = 'bing4k'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='ID')
    title = db.Column(db.String(255), unique=True, nullable=True, comment='标题')
    location = db.Column(db.String(255), unique=True, nullable=True, comment='地点')
    url = db.Column(db.String(255), unique=True, nullable=True, comment='图片地址')
    date = db.Column(db.String(255), unique=True, nullable=True, comment='日期')
