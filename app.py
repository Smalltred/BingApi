#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/4/26 21:45
from flask import Flask, render_template, make_response, jsonify
from gevent import pywsgi
from v4 import EverydayBing, params4k, params1080p
from flask_caching import Cache

files = ["1080p", "4k"]
path1080 = "/home/每日一图/1080"
path4k = "/home/每日一图/4k"

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

resolution1080 = EverydayBing(files[0], params1080p)
resolution4k = EverydayBing(files[1], params4k)


@cache.cached(timeout=43200)
@app.route("/")
def index():
    result = resolution1080.parse_response()
    return render_template("index.html", result=result)


@cache.cached(timeout=43200)
@app.route("/docs")
def readme():
    return render_template("readme.html")


@cache.cached(timeout=43200)
@app.route("/api/4k")
def image4k_json():
    result = resolution4k.parse_response()
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@cache.cached(timeout=43200)
@app.route("/api/1080")
def image1080_json():
    result = resolution1080.parse_response()
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@cache.cached(timeout=43200)
@app.route("/api/image")
def image_api():
    image_url = resolution1080.image()
    image = resolution1080.requests_url(image_url, "").content
    response = make_response(image)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@cache.cached(timeout=43200)
@app.route("/api/image/1080/")
def image_1080():
    image_url = resolution1080.image()
    image = resolution1080.requests_url(image_url, "").content
    response = make_response(image)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@cache.cached(timeout=43200)
@app.route("/api/image/4k/")
def image_4k():
    image_url = resolution4k.image()
    image = resolution4k.requests_url(image_url, "").content
    response = make_response(image)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route("/api/image/1080/1")
def imageRandom_1080():
    image_data = resolution1080.get_random_image(path1080)
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route("/api/image/4k/1")
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
