import re

str0 = 'newdream,come on!'
str1 = 'come on! newdream'
str2 = 'china1usa2german3english'
str3 = 'summer hot ~~'
# pattrn = re.compile(r'newdream') # 创建一个字符模板。r：原生字符串
pattrn0 = re.compile(r'(\w+),(\w+) (\w+)(?P<sign>.*)')  #(?P<sign>.*) 任意字符
pattrn1 = re.compile(r'come (\w+)!')
pattrn2 = re.compile(r'\d+')
pattrn3 = re.compile(r'(\w+) (\w+)')

# result1 = re.match(pattrn0,str0) # match 匹配以什么开头，0次或者多次，返回匹配对象
# result1 = re.search(pattrn1,str1)  # search 扫描整个string匹配
# result1 = re.split(pattrn2,str2) # 返回列表
# result1 = re.findall(pattrn2,str2) # 搜索string，以列表形式返回值全部能匹配的子串
# result1 = re.finditer(pattrn2,str2)  # 返回迭代器，返回一个顺序访问每一个匹配结果（match对象）的迭代器
# for r in result1:
#     print(r.group())

# print(re.sub(pattrn3,r'\2 \1',str3 )) # 替换
# str3 = re.sub(pattrn3,r'hello',str3 )
# print(str3)

# result3 = re.match(pattrn3,str3)
# print(result3.group(1).title()) # .title() 首字母大写

def fun(m):
    return m.group(1).title() + ' ' + m.group(2).title()
str3 = re.sub(pattrn3,fun,str3 )
print(str3)  # Summer Hot ~~

str4 = re.subn(pattrn3,r'\2 \1',str3 ) #('Hot Summer ~~', 1) 1是指左右替换了一次
print(str4[0])

# print(result1.string)
# print(result1.re)
# print(result1.pos) # 从第几位开始搜索
# print(result1.endpos) # 搜索到表达式结束的索引
# print(result1.lastindex)
# print('~~~~~~~~~~~~~~~~~~~~~')
# print(result1.group())
# print(result1.groups())
# print(result1.groupdict())
# print(result1.start()) #0
# print(result1.end()) #8
# print(result1.span())  #(0, 8)
# print(result1.expand(r'\1'))

# 写法二:
str5 = 'china1usa2german3english'
v_list = re.split(r'\d',str5)
print(v_list)
