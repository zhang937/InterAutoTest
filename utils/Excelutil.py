import os

import xlrd2
from utils.LogUtil import my_log


# 自定义异常类型
class SheetTypeError:
    pass


class ExcelReader:
    def __init__(self, execl_file, sheet_by):
        """
        execl 用例文件数据读取
        :param execl_file:
        :param sheet_by:
        """
        self.log=my_log()
        if os.path.exists( execl_file ):
            self.excel_file=execl_file
            self.sheet_by=sheet_by
            self._jsondata=list()
        else:
            self.log.error( f"{execl_file}文件不存在" )
            raise FileNotFoundError( f"{execl_file}文件不存在" )

    # 读取sheet
    def data(self):
        if not self._jsondata:
            workbook=xlrd2.open_workbook( self.excel_file )
            if type( self.sheet_by ) not in [int, str]:
                self.log.error( f"{self.sheet_by}is not int or str" )
                raise SheetTypeError( f"{self.sheet_by}is not int or str" )
            elif type( self.sheet_by ) == int:
                sheet=workbook.sheet_by_index( self.sheet_by )
            else:
                sheet=workbook.sheet_by_name( self.sheet_by )
            rows=sheet.nrows
            # cols=self.sheet.ncols
            title=sheet.row_values( 0 )
            for i in range( 1, rows ):
                r_values1=sheet.row_values( i )
                self._jsondata.append( dict( zip( title, r_values1 ) ) )
            self.log.info( f"数据读取结果为：{self._jsondata}" )
            return self._jsondata


if __name__ == '__main__':
    jsons=ExcelReader( '../data/requeststest.xlsx', 0 )
    t=jsons.data()
    print( t )
