import requests
from requests.exceptions import RequestException

res = requests.get(url = 'http://google.com.hk/')
print(res)

try:
    num_list = [1,2,3,4,5]
    print(num_list[6] )
except IndexError as e:
    print('索引错误')
except Exception as e:
    print('系统错误') # 不确定原因的异常卸载最后
print('hello')