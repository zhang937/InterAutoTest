import os
from utils.YamlUtil import YamlReader

# 当前文件路径
currnet=os.path.abspath( __file__ )
# 项目路径
BASE_DIR=os.path.dirname( os.path.dirname( currnet ) )
_config_path=BASE_DIR + os.sep + "config"

_config_file=_config_path + os.sep + "conf.yaml"


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


class ConfigYaml:
    def __init__(self):
        self.config=YamlReader( get_config_file() ).data()

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]


if __name__ == '__main__':
    conf_data=ConfigYaml().get_conf_url()
    print( conf_data )
