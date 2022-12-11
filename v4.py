#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/2 1:06
# @Author  : Small tred
# @FileName: v4.py
# @Software: PyCharm
# @Blog    ：https://www.hecady.com
import requests
import os
import time
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
    api = "https://cn.bing.com/HPImageArchive.aspx"
    url = "https://cn.bing.com"

    def __init__(self, path, params):
        self.path = path
        self.params = params

    def parse_response(self, response):
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

    def requestUrl(self):
        response = requests.get(self.api, self.params)
        return self.parse_response(response)

    @staticmethod
    def getImage(path):
        data = os.walk(path)
        for dir_name, dir_list, file_list in data:
            n = random.randrange(0, len(file_list))
            print(file_list[n])
            image_data = open(os.path.join(path, file_list[n]), "rb").read()
            return image_data

    def getImagePath(self):
        curr_path = os.getcwd()
        download_path = os.path.join(curr_path, self.path)
        return download_path


