#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/2 1:06
# @Author  : Small tred
# @FileName: v4.py
# @Software: PyCharm
# @Blog    ：https://www.hecady.com
import requests
import os
import random

# 获取当前目录
# 下载目录自动创建
# 分别请求4k和 1080 p
# 分别下载
# 分别写入log
params4k = {
    "format": "js",
    "idx": 0,
    "n": 1,
    "Hp": "hp",
    "FORM": "BEHPTB",
    "uhd": 1,
    "uhdwidth": 3840,
    "uhdheight": 2160,
    "nc": 1612409408851,
}

params1080p = {
    "cc": "zh",
    "format": "js",
    "idx": 0,
    "n": 1,
}


class EverydayBing:
    api = "https://www.bing.com/HPImageArchive.aspx"
    url = "https://www.bing.com"

    def __init__(self, path, params):
        self.path = path
        self.params = params

    def parse_response(self):
        response = self.requests_url(self.api, self.params)
        if response.status_code == 200:
            result = response.json()["images"][0]
            image_url = self.url + result["url"]
            image_date = result["startdate"]
            image_name = result["title"]
            image_location = result["copyright"]
            image_result = {
                "data": {
                    "url": image_url,
                    "date": image_date,
                    "title": image_name,
                    "location": image_location,
                },
                "message": "成功",
                "code": 200
            }
            return image_result
        else:
            errors = {
                "message": "失败",
                "code": 404
            }
            return errors

    def image(self):
        images_url = self.parse_response().get("data", None).get("url", None)
        return images_url

    @staticmethod
    def requests_url(url, params):
        response = requests.get(url, params)
        return response

    @staticmethod
    def get_random_image(path):
        data = os.walk(path)
        for dir_name, dir_list, file_list in data:
            n = random.randrange(0, len(file_list))
            print(file_list[n])
            image_data = open(os.path.join(path, file_list[n]), "rb").read()
            return image_data

    def get_path_image(self):
        curr_path = os.getcwd()
        download_path = os.path.join(curr_path, self.path)
        return download_path


# resolution1080 = EverydayBing("", params1080p)
# image_url = resolution1080.image()
# image = resolution1080.requestUrl(image_url, "").content
# print(image)
