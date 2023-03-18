#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/4/26 21:45
from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__, url_prefix='')


@index_bp.route("/")
def index():
    return render_template("index.html")


@index_bp.route("/docs")
def readme():
    return "未开放"
