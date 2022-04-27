#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/4/26 21:45
from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from gevent import pywsgi

from v2 import handleResult, getImage, param, param4k, path1080, path4k

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    result = handleResult(param)
    return render_template("index.html", result=result)


@app.route("/docs")
def readme():
    return render_template("readme.html")


@app.route("/api/image")
def api():
    res = request.args.get("r")
    n = request.args.get("n")
    if res is None and n is None:
        result = handleResult(param)
        return redirect(result["data"]["url"])
    else:
        if res == "1080" and n == "1":
            response = make_response(getImage(path1080))
            response.headers['Content-Type'] = 'image/png'
            return response
        elif res == ("4k" or "4K") and n == "1":
            response = make_response(getImage(path4k))
            response.headers['Content-Type'] = 'image/png'
            return response
        elif res == "1080" and n == "0":
            result = handleResult(param)
            return redirect(result["data"]["url"])
        elif res == ("4k" or "4K") and n == "0":
            result = handleResult(param4k)
            return redirect(result["data"]["url"])
        elif res == "1080" and n is None:
            result = handleResult(param)
            return redirect(result["data"]["url"])
        elif res == ("4k" or "4K") and n is None:
            result = handleResult(param4k)
            return redirect(result["data"]["url"])
        else:
            result = {
                "code": "404",
                "msg": "请求失败"
            }
            return jsonify(result)


server = pywsgi.WSGIServer(('0.0.0.0', 5244), app)
server.serve_forever()

