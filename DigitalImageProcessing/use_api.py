"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.1 16:49
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : use_api
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import tkinter as tk
from tkinter import filedialog
import base64
import requests
import json


def img_base64():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    f = open(file_path, 'rb')
    img = base64.b64encode(f.read())
    return img


def useapi():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=3s9UyhqzfBKf4uPh8cimvlYY&client_secret=rgUAdnuTIFjY1FxbRxMHL3Xv758rIEyO'
    response = requests.get(host)
    if response:
        access_token = response.json()['access_token']
    else:
        return False
    image = img_base64()
    host = 'https://aip.baidubce.com/rpc/2.0/easydl/v1/retail/recapture'
    headers = {
        'Content-Type': 'application/json'
    }
    host = host + '?access_token=' + access_token
    data = {'image': image.decode()}
    res = requests.post(url=host, headers=headers, data=json.dumps(data))
    req = res.json()
    print(req['results'])


if __name__ == '__main__':
    useapi()
