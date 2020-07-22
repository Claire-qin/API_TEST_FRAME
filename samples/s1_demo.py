from common.requests_utils import RequestsUtils

# 01）获取公众号已创建的标签
test_data_01 = [
    {'测试用例编号': 'case01', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wxb9013645f9c6f66b","secret":"8c80367d3fac3cb6d3dc910fe6416436"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
    {'测试用例编号': 'case01', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '获取公众号已创建的标签接口', '请求方式': 'get', '请求地址': '/cgi-bin/tags/get', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"id":(.+?),"name":"(.+?)"'}
]
# RequestsUtils().request_by_step(test_data_01)

# 2）创建标签->编辑标签
# {"tag":{ "id":(.+?),"name":"2020072301"}}
test_data_02 = [
    {'测试用例编号': 'case02', '测试用例名称': '测试能否成功编辑标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wxb9013645f9c6f66b","secret":"8c80367d3fac3cb6d3dc910fe6416436"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否成功编辑标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"name":"2020072310"}}', '取值方式': 'json取值', '传值变量': 'tagid', '取值代码': '$.tag.id', '期望结果类型': '无', '期望结果': ''},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否成功编辑标签', '用例执行': '否', '测试用例步骤': 'step_03', '接口名称': '编辑标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/update', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":${tagid},"name":"20200723"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"errcode":0,"errmsg":"ok"}'}
]
# RequestsUtils().request_by_step(test_data_02)

#03）# 创建标签->删除标签
test_data_03 = [
    {'测试用例编号': 'case03', '测试用例名称': '测试能否成功删除标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wxb9013645f9c6f66b","secret":"8c80367d3fac3cb6d3dc910fe6416436"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否成功删除标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"name":"2020072310"}}', '取值方式': 'json取值', '传值变量': 'tagid', '取值代码': '$.tag.id', '期望结果类型': '无', '期望结果': ''},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否成功删除标签', '用例执行': '否', '测试用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":${tagid}}} ', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"errcode":0,"errmsg":"ok"}'}
]
RequestsUtils().request_by_step(test_data_03)