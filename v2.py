#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/3/9 0:10
import requests
import os
import random

bing_api = "https://www.bing.com/HPImageArchive.aspx"
url = "https://www.bing.com"

path1080 = "D:\\其他\\图片\\bing- 1080 - 2016 - 2022-4-9"
path4k = "D:\\其他\\图片\\Bing-4K"

param = {
    "format": "js",
    "idx": 0,
    "n": 1,
    "Hp": "hp",
}

param4k = {
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


def handleResult(params):
    response = requests.get(bing_api, params=params)
    result, status = response.json(), response.status_code
    images = {
        "data":
            {
                "title": result["images"][0]["title"],
                "location": result["images"][0]["copyright"],
                "time": result["images"][0]["enddate"],
                "url": url + result["images"][0]["url"],
            },
        "status": status,
        "message": "成功",
    }
    print(images)
    return images


def getImage(path):
    data = os.walk(path)
    for dir_name, dir_list, file_list in data:
        n = random.randrange(0, len(file_list))
        print(file_list[n])
        image_data = open(os.path.join(path, file_list[n]), "rb").read()
        return image_data
