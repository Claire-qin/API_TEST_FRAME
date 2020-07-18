import ast
# sum = eval('66+32')
# print(sum)  # 98

print(ast.literal_eval("{'name':'linux','age':'18'}"))

print(eval("{'name':'linux','age':age}",{'age':18}))

age =10
print( eval("{'name':'linux','age':age}",{'age':18},locals() ) )
eval("__import__('os').system('ls')")
