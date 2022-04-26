#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/4/26 21:45
from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=80)