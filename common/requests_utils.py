#coding:utf-8
import requests,ast
import re
import jsonpath
from common.localconfig_utils import local_config

class RequestsUtils():
    def __init__(self):
        self.hosts = local_config.URL
        self.header_info = {'Content_type': 'application/json;charset=utf-8'}
        self.seesion = requests.session()
        self.temp_variables = {}

    def __get(self,get_info):
        url = self.hosts + get_info['请求地址']
        response = self.seesion.get(url = url,
                                     params =ast.literal_eval(get_info['请求参数(get)'])
                                     )
        response.encoding = response.apparent_encoding
        # 存入到变量==》存入临时字典
        if get_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),get_info['取值代码'])[0]
            self.temp_variables[ get_info['传值变量'] ] = value
            print(self.temp_variables)
        elif get_info['取值方式'] == '正则取值':
            value = re.findall(get_info['取值代码'],response.text)  #
            self.temp_variables[get_info['传值变量']] = value
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
        # print('2:',post_info['请求参数(get)'])
        response = self.seesion.post(url=url,
                                      headers=self.header_info,  # 一加就报错：AttributeError: 'tuple' object has no attribute 'items'
                                      params = ast.literal_eval(post_info['请求参数(get)']),
                                      # data=post_info['提交数据（post）']
                                      json = ast.literal_eval(post_info['提交数据（post）'])
                                      )
        response.encoding = response.apparent_encoding
        # 存入到变量==》存入临时字典
        if post_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),post_info['取值代码'])[0]
            self.temp_variables[ post_info['传值变量'] ] = value
        elif post_info['取值方式'] == '正则取值':
            value = re.findall(post_info['取值代码'],response.text)  #
            self.temp_variables[post_info['传值变量']] = value
            # print(self.temp_variables)

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
        # 取值替换:进行下一个接口请求参数的替换（url）
        param_variable_list = re.findall('\\${\w+}',step_info['请求参数(get)'])
        if param_variable_list:
            for param_variable in param_variable_list:
                step_info['请求参数(get)'] = step_info['请求参数(get)'].replace(param_variable,
                                                                        '"%s"'%self.temp_variables.get(param_variable[2:-1]))
        if request_type  == 'get':
            result = self.__get(step_info)
        elif request_type  == 'post':
            # 取值替换:post参数取值
            data_variable_list = re.findall('\\${\w+}',step_info['提交数据（post）'])
            if data_variable_list:
                for data_variable in data_variable_list:
                    step_info['提交数据（post）'] = step_info['提交数据（post）'].replace(data_variable,
                                                                            '"%s"' % self.temp_variables.get(
                                                                                data_variable[2:-1]))
            result = self.__post(step_info)
        else:
            result = {'code':3,'result':'请求方式不支持'}
        # print(result['response_body'])
        return result

    def request_by_step(self,step_infos):
        # self.temp_variables = {}
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code'] != 0:
                break
            print(temp_result['response_body'])
        return temp_result

if __name__ == '__main__':
    case_info = [
        {'请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token' },
        {'请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag" : {"name" : "nanyue_8888"}}', '取值方式': '无', '传值变量': '', '取值代码': ''}]
    RequestsUtils().request_by_step(case_info)
