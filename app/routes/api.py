#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 17:41
# @Author  : Small tred
# @FileName: api.py
# @Software: PyCharm
# @Blog    : https://www.hecady.com
from flask import Blueprint, jsonify, make_response, redirect
from app.service.service import EverydayBing, resolution1080, path1080, path4k

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.errorhandler(404)
def error_page(e):
    error = {"code": 404, "msg": "请求不合法"}
    return jsonify(error)


@api_bp.route("/api/4k")
def image4k_json():
    image = EverydayBing("", resolution="4k")
    result = image.parse_response()
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@api_bp.route("/api/4k/<int:mun>")
def image_days_4k_json(mun):
    if mun <= 8:
        image = EverydayBing("", resolution="4k", mun=mun)
        result = image.parse_response()
        response = make_response(jsonify(result))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
        return response
    else:
        return {"code": "403", "msg": "超过最大天数值"}


@api_bp.route("/1080/")
def image1080_json():
    image = EverydayBing("")
    result = image.parse_response()
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@api_bp.route("/1080/<int:mun>")
def image_days_1080_json(mun):
    if mun <= 8:
        image = EverydayBing("", mun=mun)
        result = image.parse_response()
        response = make_response(jsonify(result))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
        return response
    else:
        return {"code": "403", "msg": "超过最大天数值"}


@api_bp.route("/image")
def image_api():
    image = EverydayBing("")
    result = image.parse_response()["data"][0]["url"]
    return redirect(result)


@api_bp.route("/image/1080")
def image_1080():
    image = EverydayBing("")
    result = image.parse_response()["data"][0]["url"]
    return redirect(result)


@api_bp.route("/image/4k")
def image_4k():
    image = EverydayBing("", resolution="4k")
    result = image.parse_response()["data"][0]["url"]
    return redirect(result)


@api_bp.route("/image/1080/r")
def imageRandom_1080():
    image_data = resolution1080.get_random_image(path1080)
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@api_bp.route("/image/4k/r")
def imageRandom_4k():
    image_data = EverydayBing.get_random_image(path4k)
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response
