import os
from common.excel_untils import ExcelUtils
from common import config  # 方法一
from common.localconfig_utils import local_config # 方法二
from common.sql_utils import SqlUtils

test_data_path = os.path.join(os.path.dirname(__file__),'..',local_config.CASE_DATA_PATH)

class TestdataUtils():
    def __init__(self,test_data_path=test_data_path):
        self.test_data_path= test_data_path
        self.test_data = ExcelUtils(test_data_path,'Sheet1').get_sheet_data_by_dict() # 取全部数据
        self.test_data_my_mysql = SqlUtils().get_mysql_test_case_info() # mysql的数据

    def __get_testcase_data_by_dict(self):
        test_case_dict = {}
        for row_data in self.test_data:
            test_case_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict

    def get_testcase_data_list(self):
        testcase_list = []
        for k, v in self.__get_testcase_data_by_dict().items():
            one_case_dict = {}
            one_case_dict['case_id'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list

    def __get_testcase_data_dict_by_mysql(self):
        test_case_dict = {}
        for row_data in self.test_data_my_mysql:
            test_case_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict

    def get_testcase_data_list_by_mysql(self):
        testcase_list = []
        for k, v in self.__get_testcase_data_dict_by_mysql().items():
            one_case_dict = {}
            one_case_dict['case_id'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list

if __name__ == '__main__':
    testdatautils = TestdataUtils()
    for i in testdatautils.get_testcase_data_list_by_mysql():
        print(i)
