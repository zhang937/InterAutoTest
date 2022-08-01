"""
模块返回各种路径和conf.yml配置
"""
import os
from utils.YamlUtil import YamlReader

# 当前文件路径
currnet=os.path.abspath( __file__ )
# 项目路径
BASE_DIR=os.path.dirname( os.path.dirname( currnet ) )
_config_path=BASE_DIR + os.sep + "config"
_data_config_path=BASE_DIR + os.sep + "data"

_config_file=_config_path + os.sep + "conf.yml"

_db_config_file=_config_path + os.sep + "db_conf.yml"

_log_path=BASE_DIR + os.sep + "logs"


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def get_log_path():
    return _log_path

def get_db_conf_file():
    return _db_config_file

def get_data_path():
    return _data_config_path

class ConfigYaml:
    def __init__(self):
        self.config=YamlReader( get_config_file() ).data()
        self.db_config=YamlReader(get_db_conf_file()).data()

    def get_conf_url(self):
        """

        :return:
        """
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """

        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """

        :return:
        """
        return self.config["BASE"]["log_extension"]

    def get_db_conf_info(self,db_alias):
        """

        :return:
        """
        return self.db_config[db_alias]
    def get_execl_file(self):
        """

        :return:
        """
        return self.config["BASE"]["test"]["case_file"]

    def get_execl_sheet(self):
        """

        :return:
        """
        return self.config["BASE"]["test"]["case_sheet"]

if __name__ == '__main__':
    conf_data=ConfigYaml().get_conf_log()
    # conf_data1=ConfigYaml().get_conf_log_extension()
    # conf_data2=ConfigYaml().get_db_conf_info('env-1')
    conf_data1=ConfigYaml().get_execl_file()
    conf_data2=ConfigYaml().get_execl_sheet()
    print(conf_data1,conf_data2)

