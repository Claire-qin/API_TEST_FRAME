# case_list.setdefault()
lista = [
    {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02'},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02'}
]

case_dict={}
for i in lista:
    case_dict.setdefault(i['测试用例编号'],[]).append(i)  # 核心：不覆盖，可以append往后面追加1条
# print(case_dict)

# 字典转列表
case_list = []
for k,v in  case_dict.items():
    case_dict={}
    case_dict['case_name'] = k
    case_dict['case_indo'] = v
    case_list.append(case_dict)

for c in case_list:
    print(c)