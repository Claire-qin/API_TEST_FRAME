import unittest,paramunittest
import warnings
from common.testdata_utils import TestdataUtils
from common.requests_utils import RequestsUtils

# case_info = TestdataUtils().get_testcase_data_list() # excel数据
case_info = TestdataUtils().get_testcase_data_list_by_mysql() #mysql数据
@paramunittest.parametrized(
    *case_info
)
class APITest(paramunittest.ParametrizedTestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
    def setParameters(self, case_id, case_info):
        self.case_id = case_id
        self.case_info = case_info
    def test_api_common_function(self):
        """
        测试描述
        """
        self._testMethodName = self.case_info[0].get('测试用例编号') # 编号和说明符重新定义
        self._testMethodDoc = self.case_info[0].get('测试用例名称')
        actual_result = RequestsUtils().request_by_step(self.case_info)
        self.assertTrue(actual_result.get('check_result'),actual_result.get('message'))

if __name__ == '__main__':
    unittest.main()