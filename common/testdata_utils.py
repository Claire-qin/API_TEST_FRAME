import os
from common.excel_untils import ExcelUtils

test_data_path = os.path.join(os.path.dirname(__file__),'..','samples/test_data/test_case.xlsx')

class TestdataUtils():
    def __init__(self,test_data_path=test_data_path):
        self.test_data_path= test_data_path
        self.test_data = ExcelUtils(test_data_path,'Sheet1').get_sheet_data_by_dict() # 取全部数据

    def __get_testcase_data_by_dict(self):
        test_case_dict = {}
        for row_data in self.test_data:
            test_case_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict

    def get_testcase_data_list(self):
        testcase_list = []
        for k, v in self.__get_testcase_data_by_dict().items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_indo'] = v
            testcase_list.append(one_case_dict)
        return testcase_list

if __name__ == '__main__':
    testdatautils = TestdataUtils()
    for i in testdatautils.get_testcase_data_list():
        print(i)
