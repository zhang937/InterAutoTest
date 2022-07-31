import pytest
from utils.LogUtil import my_log

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

    data=[{"name":"zhangsan","age":3}, {"name":"lisi","age":4}]

    # @pytest.mark.flaky(reruns=2,reruns_delay=2)
    @pytest.mark.parametrize( "datas", data )
    def test_noteq(self, datas):
        log.info( f"不等于校验{datas['name']}" )
        assert sum( datas['age'] ) == 4


if __name__ == '__main__':
    pytest.main( )
