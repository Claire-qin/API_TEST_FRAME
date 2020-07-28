import pymysql

connect = pymysql.connect(host = '127.0.0.1',
                          port =3306,
                          user = 'root',
                          password = 'root',
                          database = 'api_test',
                          charset = 'utf8')

cur = connect.cursor(cursor= pymysql.cursors.DictCursor) # 连接加cursor= pymysql.cursors.DictCursor  返回字典形式
str = """
select case_info.case_id as '测试用例编号',case_info.case_name as '测试用例名称',case_info.is_run '用例执行',case_step_info.case_step_name '测试用例步骤',api_info.api_name '接口名称',api_info.api_request_type '请求方式',api_info.api_request_url '请求地址',api_info.api_url_params '请求参数(get)',api_post_data '提交数据（post）',case_step_info.get_value_type '取值方式',case_step_info.variable_name '传值变量',case_step_info.get_value_code '取值代码',case_step_info.excepted_result_type '期望结果类型',case_step_info.excepted_result '期望结果'
from case_step_info 
LEFT JOIN case_info on case_step_info.case_id = case_info.case_id
LEFT JOIN api_info on case_step_info.api_id = api_info.api_id 
where case_info.is_run = '是'
order by case_info.case_id,case_step_info.case_step_name;
"""
cur.execute(str)
for step in cur.fetchall():
    print(step)



