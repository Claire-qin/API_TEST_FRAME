import requests
import re
from common.localconfig_utils import *

URL = LocalconfigUtils().URL
session = requests.session()

# 1)注册页面
register_page_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/json;v=b3;q=0.9",
    "X-Requested-With":"XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
register_page_get_param = {
    "m": "u",
    "c": "register"
}
register_page_res = session.get(URL+'/phpwind/index.php',
                                     params=register_page_get_param,
                                     headers=register_page_headers)
register_page_body = register_page_res.content.decode('utf-8')
csrf_token = re.findall('name="csrf_token" value="(.+?)"/>', register_page_body)[0]
# print(csrf_token)

# 2) 注册
register_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/json;v=b3;q=0.9",
    "X-Requested-With":"XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
register_get_params={
    "m": "u",
    "c": "register",
    "a": "dorun"
}
register_data = {
    "username": "qch2020071504",
    "password": "123456",
    "repassword": "123456",
    "email": "qch2020071504@qq.com",
    "csrf_token":csrf_token
}
register_res = session.post(url = URL+'/phpwind/index.php',
                            headers = register_headers,
                            params = register_get_params,
                            data = register_data )
print( register_res.content.decode('unicode_escape') )