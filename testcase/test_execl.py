from config.Conf import ConfigYaml
from common.ExeclData import Data
from utils.LogUtil import my_log
from common import ExeclConfig
import os
import pytest

# def test_base():
case_file=os.path.join( "../data", ConfigYaml().get_execl_file() )
print( case_file )
sheet_name=ConfigYaml().get_execl_sheet()
print( sheet_name )
run_list=Data( case_file, sheet_name ).get_run_data()
print( run_list )
log=my_log()


class Test_Execl:
    # @classmethod
    def test_run(self):
        data_key=ExeclConfig.DataConfig
        url=ConfigYaml().get_conf_url()+run_list[0][data_key.url]
        print( url )
        #初始化请求参数
        # case_id ……


# TestExecl().test_run()
if __name__ == '__main__':
    pytest.main( ["test_execl.py"] )
