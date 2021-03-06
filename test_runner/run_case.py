import os
import unittest
from common.localconfig_utils import local_config
from common import HTMLTestReportCN
from common.email_utils import EmailUtils

current_path = os.path.dirname(__file__)
test_case_path =  os.path.join(current_path,'..',local_config.CASE_PATH)
test_report_path =  os.path.join(current_path,'..',local_config.REPORT_PATH)

class RunCase():
    def __init__(self):
        self.test_case_path = test_case_path
        self.report_path  = test_report_path
        self.title = 'P1P2接口自动化测试报告'
        self.description = '自动化接口测试框架学习'
        self.tester = '测试开发组全体成员'

    def load_test_suite(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='api_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        return all_suite

    def run(self):
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_file_path,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester=self.tester)
        runner.run(self.load_test_suite())
        fp.close()
        return report_file_path
#
if __name__ == '__main__':
    report_path = RunCase().run()
    EmailUtils('<h3 align="center">自动化测试报告</h3>',report_path).send_mail()
    # EmailUtils(open(report_path,'rb').read(),report_path).send_mail()




