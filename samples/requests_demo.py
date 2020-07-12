# 公众号创建标签

import requests

hosts = 'https://api.weixin.qq.com'

# 获取access_token
params={
    'grant_type':'client_credential',
    'appid':'wxb9013645f9c6f66b',
    'secret':'8c80367d3fac3cb6d3dc910fe6416436'
}
res01 = requests.get(url = hosts+'/cgi-bin/token',
                     params = params )
access_token = res01.json()['access_token']

# 创建一个标签
get_params={
    'access_token':access_token
}
post_params ='{"tag" : { "name" : "20200712_001"   } }'
headers = {
    'content_type':'application/json'
}
res_02 = requests.post(url = hosts+'/cgi-bin/tags/create',
                       params = get_params,
                       data =  post_params, # post的参数用data描述)
                       headers = headers
                       )
print(res_02.json())

