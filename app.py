#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/4/26 21:45
from flask import Flask, render_template, make_response, jsonify, redirect
from gevent import pywsgi
from v4 import EverydayBing
from flask_caching import Cache

files = ["1080p", "4k"]
path1080 = "/home/每日一图/1080"
path4k = "/home/每日一图/4k"

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

resolution1080 = EverydayBing(files[0])
resolution4k = EverydayBing(files[1], 0, )


@app.errorhandler(404)
def error_page(e):
    error = {"code": 404, "msg": "请求不合法"}
    return jsonify(error)


@cache.cached(timeout=43200)
@app.route("/")
def index():
    image = EverydayBing("")
    result = image.parse_response()[0]
    return render_template("index.html", result=result)


@cache.cached(timeout=43200)
@app.route("/docs")
def readme():
    return render_template("readme.html")


@cache.cached(timeout=43200)
@app.route("/api/4k")
def image4k_json():
    image = EverydayBing("", resolution="4k")
    result = image.parse_response()
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@cache.cached(timeout=43200)
@app.route("/api/4k/<int:mun>")
def image_days_4k_json(mun):
    if mun <= 8:
        image = EverydayBing("", resolution="4k", mun=mun)
        result = image.parse_response()
        return jsonify(result)
    else:
        return {"code": "403", "msg": "超过最大天数值"}


@cache.cached(timeout=43200)
@app.route("/api/1080/")
def image1080_json():
    image = EverydayBing("")
    result = image.parse_response()
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@cache.cached(timeout=43200)
@app.route("/api/1080/<int:mun>")
def image_days_1080_json(mun):
    if mun <= 8:
        image = EverydayBing("", mun=mun)
        result = image.parse_response()
        return jsonify(result)
    else:
        return {"code": "403", "msg": "超过最大天数值"}


@app.route("/api/image/")
@cache.cached(timeout=43200)
def image_api():
    image = EverydayBing("")
    result = image.parse_response()["data"][0]["url"]
    return redirect(result)


@cache.cached(timeout=43200)
@app.route("/api/image/1080/")
def image_1080():
    image = EverydayBing("")
    result = image.parse_response()["data"][0]["url"]
    return redirect(result)


@cache.cached(timeout=43200)
@app.route("/api/image/4k/")
def image_4k():
    image = EverydayBing("", resolution="4k")
    result = image.parse_response()["data"][0]["url"]
    return redirect(result)


@app.route("/api/image/1080/random")
def imageRandom_1080():
    image_data = resolution1080.get_random_image(path1080)
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route("/api/image/4k/random")
def imageRandom_4k():
    image_data = EverydayBing.get_random_image(path4k)
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


server = pywsgi.WSGIServer(('0.0.0.0', 5223), app)
server.serve_forever()
