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


@app.route("/api/4k")
def image4k_json():
    result = handleResult(param4k)
    return jsonify(result)


@app.route("/api/1080")
def image1080_json():
    result = handleResult(param)
    return jsonify(result)


@app.route("/api/image")
def image_api():
    result = handleResult(param)
    return redirect(result["data"]["url"])


@app.route("/api/image/1080/")
def image_1080():
    result = handleResult(param)
    return redirect(result["data"]["url"])


@app.route("/api/image/4k/")
def image_4k():
    result = handleResult(param4k)
    return redirect(result["data"]["url"])


@app.route("/api/image/1080/1")
def imageRandom_1080():
    response = make_response(getImage(path1080))
    response.headers['Content-Type'] = 'image/png'
    return response


@app.route("/api/image/4k/1")
def imageRandom_4k():
    response = make_response(getImage(path4k))
    response.headers['Content-Type'] = 'image/png'
    return response


server = pywsgi.WSGIServer(('0.0.0.0', 5244), app)
server.serve_forever()
