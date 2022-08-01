import pytest
from utils.LogUtil import my_log
from utils.AssertUtil import AssertUtil
from common.Base import init_db

log=my_log()


def sum(x):
    return x + 1



class Test_Func:
    def setup_class(self):
        log.info( "_______setup_class______" )


    def teardown_class(self):
        log.info( "_______teardown_class______" )

    def setup(self):
        log.info( "_______setup______" )

    def teardown(self):
        log.info( "_______teardown______" )

    data=[("zhangsan",3), ("lisi",4)]

    # @pytest.mark.flaky(reruns=2,reruns_delay=2)
    # @pytest.mark.parametrize( ("name","age"), data )
    @pytest.mark.skip( reason='不执行' )
    def test_noteq(self, name,age):
        log.info( f"不等于校验name" )
        test=sum( age )
        AssertUtil().assert_body(test,4)

    def test_mysql(self):
        sql="select name,password from systest.user_info where 0=0 and name='root';"
        env='env-1'
        testsql=init_db(env)
        log.info(f"登录数据库环境{env}成功")
        result=testsql.fetchone(sql)
        log.info( f"数据库验证,{result}" )
        AssertUtil().assert_body(result['name'],'root')


if __name__ == '__main__':
    pytest.main( )
