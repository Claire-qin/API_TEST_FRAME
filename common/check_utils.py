# 断言封装：4种形式
import ast,re

class CheckUtils():
    def __init__(self,check_response = None):
        self.ck_response = check_response
        self.ck_rules = {
            '无':self.no_check,
            'json键是否存在':self.check_key,
            'json键值对':self.check_keyvalue,
            '正则匹配':self.check_regexp
        }
        self.pass_result = {
            'code': 0,  # 标志位，请求是否成功
            'response_reason': self.ck_response.reason,  # 响应行
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,  # 响应头
            'response_body': self.ck_response.text,  # 响应正文
            'check_result':True,
            'message':'case excute pass' # 扩展,作为日志输出等
        }
        self.fail_result = {
            'code': 2,  # 标志位，请求是否成功
            'response_reason': self.ck_response.reason,  # 响应行
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,  # 响应头
            'response_body': self.ck_response.text, # 响应正文
            'check_result':False,
            'message':'' # 扩展,作为日志输出等
        }
# 无
    def no_check(self,check_data=None):  # check_data=None 统一，不会报错。用不到。
        return self.pass_result
# json的键是否存在
    def check_key(self,check_data = None):
        check_data_list = check_data.split(',')
        # print(check_data_list)
        res_list = [] # 存放每次比较的结果
        wrong_key = [] # 存放比较失败的key
        for check_data in check_data_list:
            if check_data in self.ck_response.json().keys():
                res_list.append(self.pass_result)
            else :
                res_list.append(self.fail_result)
                wrong_key.append(check_data)  # 错误数据放进去
        # print(relist)
        # print(wrongkey)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result
# json键值对
    def check_keyvalue(self,check_data = None):
        res_list = [] # 存放每次比较的结果
        wrong_items = [] # 存放比较失败的键值对
        for check_item in ast.literal_eval(check_data).items(): # 每一项键值对
            if check_item in self.ck_response.json().items():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_items.append(check_data)
        # print(res_list)
        # print(wrong_items)
        if  self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

# 正则
    def  check_regexp(self,check_data = None):
        pattern = re.compile(check_data) # 创建一个字符模板。
        # result_01 = re.findall(pattern=pattern,string=self.ck_response.text)
        # print(result_01)
        if re.findall(pattern=pattern,string=self.ck_response.text):  # 搜索string，以列表形式返回值全部能匹配的子串
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self,check_type=None,check_data=None):
        code = self.ck_response.status_code
        if code == 200:
            if check_type in self.ck_rules.keys():
                result = self.ck_rules[check_type](check_data) # 后面加（）,就可以调用这个方法。他会取一个值（如：self.check_keyvalue）。调用方法
                return result
            else:
                self.fail_result['massage'] = '不支持%s这种判断方式'%check_type
                return self.fail_result
        else:
            self.fail_result['message'] = '请求的响应状态码%s'%str(code)
            return self.fail_result


if __name__ == '__main__':
    # CheckUtils({"access_token":"hello","expire_in":7200}).check_key('access_token,expire_in')
    # CheckUtils({"access_token":"hello","expire_in":7200}).check_keyvalue('{"expire_in":7200}')
    print(CheckUtils('{"access_token":"hello","expire_in":7200}').check_regexp('"access_token":"(.+?)"'))
    # s = {"access_token":"hello","expire_in":7200}
    # print(list(s.keys()))

    # str1= '{"access_token":"hello","expire_in":7200}'
    # pattern = re.compile('"access_token":"(.+?)"')
    # print(re.findall(pattern,str1))
    # if []:
    #     print('hello')