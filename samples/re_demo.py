import re

str1 = 'newdream,come on!'
# pattrn = re.compile(r'newdream') # 创建一个字符模板。r：原生字符串
pattrn = re.compile(r'(\w+),(\w+) (\w+)(?P<sign>.*)')  #(?P<sign>.*) 任意字符

result1 = re.match(pattrn,str1) # match 匹配以什么开头，0次或者多次，返回匹配对象
print(result1.string)
print(result1.re)
print(result1.pos) # 从第几位开始搜索
print(result1.endpos) # 搜索到表达式结束的索引
print(result1.lastindex)
print('~~~~~~~~~~~~~~~~~~~~~')
print(result1.group())
print(result1.groups())
print(result1.groupdict())
print(result1.start()) #0
print(result1.end()) #8
print(result1.span())  #(0, 8)
print(result1.expand(r'\2 \3 \1 \4'))
