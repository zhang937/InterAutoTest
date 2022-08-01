from utils.Excelutil import ExcelReader
from common.ExeclConfig import DataConfig


class Data:
    def __init__(self,testcase_file,sheet_name):
        self.reader=ExcelReader( testcase_file, sheet_name)
        self.is_run=DataConfig.is_run

    def get_run_data(self):
        run_list=list()
        for line in self.reader.data():
            if str(line[self.is_run]).lower() == 'y':
                run_list.append(line)
        return run_list
if __name__ == '__main__':
    aa=Data()