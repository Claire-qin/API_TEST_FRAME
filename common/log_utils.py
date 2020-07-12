import os
import logging
import time
from common.localconfig_utils import local_config

log_output_path = os.path.join(os.path.dirname(__file__),'..',local_config.LOG_PATH)

class LogUtils():
    def __init__(self,log_path=log_output_path):
        self.log_name = os.path.join(log_output_path,'ApiTest_%s.log'%time.strftime('%Y_%m_%d'))  # 路径下 每天生成文件
        self.logger = logging.getLogger('ApiTestLog')
        self.logger.setLevel(local_config.LOG_LEVEL)

        console_handler = logging.StreamHandler() #控制台输出
        file_handler = logging.FileHandler(self.log_name,'a','utf-8')  # 文件输出
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()  # 防止日志重复
        file_handler.close()

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger() # 防止日志重复

if __name__ == '__main__':
    logger.info('hello')
