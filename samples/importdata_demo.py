# 使用excel中的数据去驱动 requests_utils
from common.testdata_utils import TestdataUtils
from common.requests_utils import RequestsUtils

all_case_info = TestdataUtils().get_testcase_data_list()
# 单个执行
case_info = all_case_info[4].get('case_info') #取数据
print(case_info)
RequestsUtils().request_by_step(case_info)

# 全部执行
# for case_info in all_case_info:
#     RequestsUtils().request_by_step(case_info.get('case_info'))

