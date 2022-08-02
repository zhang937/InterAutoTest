import pytest
import allure

import subprocess


@allure.feature("接口测试，只是用一级标签")
class TestAllure:
    @allure.title( "测试用例标题1" )
    @allure.description( "测试用例1,打印" )
    @allure.story("只是一个二级标签")
    @allure.severity( allure.severity_level.TRIVIAL )
    def test_1(self):
        print( "test1" )


    @allure.title( "测试用例标题2" )
    @allure.description( "测试用例2,打印" )
    @allure.story( "只是一个二级标签" )
    @allure.severity( allure.severity_level.CRITICAL )
    def test_2(self):
        print( "test2" )


    @allure.title( "测试用例标题3" )
    @allure.description( "测试用例3,打印" )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_3(self):
        print( "test3" )

    @pytest.mark.parametrize("case",["Zhangsan","lisi"])
    def test_4(self,case):
        print(f"this is a {case}")
        desc=f"<font color='red'>this Test <Br/> Name is </font> <span>{case}"
        # allure.dynamic.title(desc)
        allure.dynamic.description(desc )
        # allure.dynamic.feature( f"this Test Name is  {case}" )
        # allure.dynamic.story( f"this Test Name is  {case}" )



if __name__ == '__main__':
    # pytest.main( ["alluretest.py"] )
    subprocess.call(["ls",'-l'])