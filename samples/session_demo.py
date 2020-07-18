# 用requests完成论坛的发帖

import requests
import re
from collections import OrderedDict

hosts = 'http://47.107.178.45'
session = requests.session()

# 01、进入论坛首页
res01 = session.get(url = hosts+'/phpwind/')
body01 = res01.content.decode('utf-8')
token_id = re.findall('name="csrf_token" value="(.+?)"/>',body01)[0]
# print(token_id)

# 02、提交用户名和密码
get_params={
    "m": "u",
    "c": "login",
    "a": "dologin"
}
form_data = {
    "username": "xiaoliusir001",
    "password": "123456",
    "csrf_token": token_id,
}

headers_info = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9"
}
res02 = session.post(url = hosts+'/phpwind/index.php',
                      params = get_params,
                      data = form_data,
                      headers = headers_info)
body02 = res02.content.decode('utf-8')
login_id = re.findall('_statu=(.+?)"',body02)[0]
print(login_id)

# 3）登录后的授权
get_params = {
    "m":"u",
    "c":"login",
    "a":"welcome",
    "_statu":login_id
}
res03 = session.get( url = hosts + '/phpwind/index.php',
                     params = get_params
                     )
# print( res03.content.decode('utf8') )

# 4)发帖
get_params = {
    "c":"post",
    "a":"doadd",
    "_json":1,
    "fid":80
}
headers_info = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryAS42cPv6bKiOKp1e",
    "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"zh-CN,zh;q=0.9"
}
mul_form_data = OrderedDict(
    [
        ("atc_title", (None, 'P1P2P3222')),
        ("atc_content", (None, 'hello,PPP3444')),
        ('pid', (None, '')),
        ('tid', (None, '')),
        ('special', (None, 'default')),
        ('reply_notice', (None, '1')),
        ('csrf_token', (None, token_id))
     ]
)
res04 = session.post( url = hosts + '/phpwind/index.php',
                      headers = headers_info,
                      params = get_params,
                      files = mul_form_data
                      )
print( res04.content.decode('utf8') )


