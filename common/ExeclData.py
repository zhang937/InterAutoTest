from utils.Excelutil import ExcelReader
from common.ExeclConfig import DataConfig


class Data:
    def __init__(self, testcase_file, sheet_name):
        self.reader=ExcelReader( testcase_file, sheet_name )
        self.is_run=DataConfig.is_run

    def get_run_data(self):
        """
        获取自动化用例
        :return:
        """
        run_list=[line for line in self.reader.data() if str( line[self.is_run] ).lower() == 'y']
        return run_list

    def get_case_list(self):
        """
        获取全部用例
        :return:
        """
        all_list=[ line for line in self.reader.data()]
        return all_list
    def get_case_pre(self,pre):
        """
        根据前置条件，从全局用例中取用例。
        :param pre:
        :return:
        """
        all_list=self.get_case_list()
        pre_case=[line for line in all_list if pre in dict[line].values()]
        return  pre_case

if __name__ == '__main__':
    aa=Data()
