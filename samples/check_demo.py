# 断言封装---》正则匹配测试
import re,ast

# 实际结果
str1 = '{"access_token":"35_uLzM4a0CSbx2pd_Dj_0WJ7hEwF6n5Lq5DrKw-SiLoKh1y1dLG3K37uBxKUVYaO7sDi6mI23MkIsVKixj08D_btzHv3oijZL7zWTtjRVH093S2IE8zZtkpm1GM79pr2bPUVm_pTY9GE8iDAZgXFXdAAAFNF","expires_in":7200}'
# 期望结果：
str2 = '{"access_token":"(.+?)","expires_in":(.+?)}'

# 一：正则
if re.findall(str2,str1):
    True
    print(re.findall(str2, str1))  # 模板 要找的字符串 [("XXX"),("XXX")]
else:
    print(False)

# 二：是否包含json键:多个都对，值显示一个。有一个错了，就不执行了。
jsondata1 = ast.literal_eval(str1) # 转成字典
str2 = 'access_token,expires_in'
check_key_list = str2.split(',')
print(check_key_list)
for check_key in check_key_list:
    result = True
    if check_key in jsondata1.keys():
        result = True
    else:
        result = False
    if not result: # 有一个错了，就不执行了
        break
# print(result)

# 三：键值对值都相等的情况
str3 = '{"expires_in":7200}'
for v in ast.literal_eval(str3).items(): # 返回项
    result = True
    if v in jsondata1.items():
        result = True
    else:
        result = False
    if not result:
        break
print(result)



