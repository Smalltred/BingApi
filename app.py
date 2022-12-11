#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/4/26 21:45
from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from gevent import pywsgi
from v4 import EverydayBing, params4k, params1080p

files = ["1080p", "4k"]
path1080 = "/home/每日一图/1080"
path4k = "/home/每日一图/4k"

app = Flask(__name__)
app.debug = True
app.config["JSON_AS_ASCII"] = False

resolution4k = EverydayBing(files[0], params1080p)
resolution1080 = EverydayBing(files[1], params4k)


@app.route("/")
def index():
    result = resolution1080.requestUrl()
    return render_template("index.html", result=result)


@app.route("/docs")
def readme():
    return render_template("readme.html")


@app.route("/api/4k")
def image4k_json():
    result = resolution4k.requestUrl()
    return jsonify(result)


@app.route("/api/1080")
def image1080_json():
    result = resolution1080.requestUrl()
    return jsonify(result)


@app.route("/api/image")
def image_api():
    result = resolution1080.requestUrl()
    return redirect(result["data"]["url"])


@app.route("/api/image/1080/")
def image_1080():
    result = resolution1080.requestUrl()
    return redirect(result["data"]["url"])


@app.route("/api/image/4k/")
def image_4k():
    result = resolution4k.requestUrl()
    return redirect(result["data"]["url"])


@app.route("/api/image/1080/1")
def imageRandom_1080():
    image_data = resolution1080.getImage(path1080)
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response


@app.route("/api/image/4k/1")
def imageRandom_4k():
    image_data = EverydayBing.getImage(path4k)
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response


server = pywsgi.WSGIServer(('0.0.0.0', 5244), app)
server.serve_forever()
