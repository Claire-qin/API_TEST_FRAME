# 方式一：2个文件写
import os
from common.config_utils import ConfigUtils
import configparser

config_path = os.path.join(os.path.dirname(__file__),'..','conf/config.ini')
configutils = ConfigUtils(config_path)

URL = configutils.read_value('default','URL')
CASE_DATA_PATH = configutils.read_value('path','CASE_DATA_PATH')