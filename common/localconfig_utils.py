# 方法二：
import os
import configparser

config_path = os.path.join(os.path.dirname(__file__),'..','conf/config.ini')

class LocalconfigUtils():
    def __init__(self,config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path,encoding='utf-8')

    # 直接写业务
    @property # 修饰器：把方法变为属性方法
    def URL(self):
        url_value =  self.cfg.get('default','URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path_value = self.cfg.get('path','CASE_DATA_PATH')
        return case_data_path_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('path','LOG_PATH')
        return log_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int(self.cfg.get('log', 'LOG_LEVEL'))
        return log_level_value

local_config = LocalconfigUtils()

if __name__ == '__main__':
    print(local_config.CASE_DATA_PATH)