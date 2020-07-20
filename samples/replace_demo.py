import requests,ast,re

temp_variable = {'token':'hello'}
params = '{"access_token":${token}}'  # 建议考虑一个以上的情况
value= re.findall('\\${\w+}',params)[0]
print(value)
params = params.replace(value,'"%s"'%temp_variable[value[2:-1]]) # 老的字符串 替换成 新的
print(params)

# 替换：思路一
temp_variable_02 = {'token':'123456','number':'123','age':'66'}
str1 = '{"access_token":${token},${age}==>${number}'
for v in re.findall('\\${\w+}',str1):
    print(v )
    str1 = str1.replace(v, '"%s"'%temp_variable_02[v[2:- 1]])
print(str1)

# # 不可用
# str1 = re.sub('\\${\w+}',r'123456',str1)
# print(str1) #{"access_token":123456,123456==>123456


# requests.get('/cgi-bin/tags/delete',
#              params = ast.literal_eval(params))
