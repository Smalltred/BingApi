#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/2 1:06
# @Author  : Small tred
# @FileName: service.py
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


class EverydayBing:
    api = "https://www.bing.com/HPImageArchive.aspx"
    url = "https://www.bing.com"

    def __init__(self, path, resolution="1080", mun=1):
        self.path = path
        self.params = {
            "cc": "zh",
            "format": "js",
            "idx": 0,
            "n": mun,  # 最多八张图片
            "Hp": "hp",  # 固定参数
            "uhd": 1,  # 高清
        }
        if resolution == "4k":
            self.params["uhdwidth"] = 3840
            self.params["uhdheight"] = 2160
        if mun > 8:
            self.params["n"] = 8

    def parse_response(self):
        data = []
        image_result = []
        response = requests.get(self.api, self.params)
        if response.status_code == 200:
            result = response.json()["images"]
            if len(result) >= 1:
                for i in range(0, len(result)):
                    image_url = self.url + result[i]["url"]
                    image_date = result[i]["enddate"]
                    image_name = result[i]["title"]
                    image_location = result[i]["copyright"]
                    temp = {
                        "url": image_url,
                        "date": image_date,
                        "title": image_name,
                        "location": image_location,
                    }

                    data.append(temp)
                image_result = {"message": "成功", "code": 200, "data": data}
            return image_result
        else:
            errors = {
                "message": "失败",
                "code": 404
            }
        return errors

    def image(self):
        images_url = self.parse_response().get("data", None)[0].get("url", None)
        return images_url

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


files = ["1080p", "4k"]
path1080 = "/home/每日一图/1080"
path4k = "/home/每日一图/4k"

resolution1080 = EverydayBing(files[0], "1080")
resolution4k = EverydayBing(files[1], "4k")

