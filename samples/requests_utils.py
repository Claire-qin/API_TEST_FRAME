#coding:utf-8
import requests,ast
import jsonpath
from common.localconfig_utils import local_config
class RequestsUtils():
    def __init__(self):
        self.hosts = local_config.URL
        self.headers = {'content_type': 'application/json;charset=utf-8'},
        self.seesions = requests.session()
        self.temp_variables = {}

    def __get(self,get_info):
        url = self.hosts + get_info['请求地址']
        response = self.seesions.get(url = url,
                                     params =ast.literal_eval(get_info['请求参数(get)'])
                                     )
        response.encoding = response.apparent_encoding
        if get_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),get_info['取值代码'])[0]
            self.temp_variables[ get_info['传值变量'] ] = value
            # print(self.temp_variables)

        result = {
            'code':0, # 标志位，请求是否成功
            'response_reason':response.reason, # 响应行
            'response_code':response.status_code,
            'response_headers':response.headers,  # 响应头
            'response_body':response.text # 响应正文
        }
        return result

    def __post(self,post_info):
        url = self.hosts + post_info['请求地址']
        response = self.seesions.post(url=url,
                                      # headers=self.headers,  # 一加就报错：AttributeError: 'tuple' object has no attribute 'items'
                                      params = {"access_token":"35_DVSMbr3QAtrnoBKBFndtUMXKFrEYALv_PmSXoZlZOOCpYafjHtr6A8SqiXWsMDhpjB0EqoHLvWL_r0FQ_kzcDzolzzUxOxVBbpkO3q2CwU4RLdo1wK013LMicNqedPbE83K9FkPTSaPzRAdyIYBgAHAAQT"},
                                      # params = ast.literal_eval(post_infos['请求参数(get)']),
                                      data=post_info['提交数据（post）']
                                      # json =ast.literal_eval(post_infos['提交数据（post）'])
                                      )
        response.encoding = response.apparent_encoding
        if post_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),post_info['取值代码'])[0]
            self.temp_variables[ post_info['传值变量'] ] = value

        result = {
            'code': 0,  # 标志位，请求是否成功
            'response_reason': response.reason,  # 响应行
            'response_code': response.status_code,
            'response_headers': response.headers,  # 响应头
            'response_body': response.text  # 响应正文
        }
        return result

    def request(self,step_info):
        request_type = step_info['请求方式']
        if request_type  == 'get':
            result = self.__get(step_info)
        elif request_type  == 'post':
            result = self.__post(step_info)
        else:
            result = {'code':3,'result':'请求方式不支持'}
        # print(result['response_body'])
        return result

    def request_by_step(self,step_infos):
        for step_info in step_infos:
            result = self.request(step_info)
            if result['code'] != 0:
                break
        return result

if __name__ == '__main__':
    get_infos = {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'}
    # get_infos ={'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in'}
    RequestsUtils().request(get_infos)
    # 字符串 转 字典 eval函数
    # post_infos = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":120}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}'}
    # RequestsUtils().post(post_infos)

    # case_info = [{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'}, {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag" : {"name" : "衡东8888"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"衡东8888"}}'}]
    # requestsUtils = RequestsUtils()
    # for c in case_info:
    #     requestsUtils.request(c)