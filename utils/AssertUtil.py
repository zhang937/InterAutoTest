from utils.LogUtil import my_log
from utils.BaseUtil import get_item_by_key
import json


class AssertUtil:
    def __init__(self):
        self.log=my_log()

    def assert_code(self, code, expected_code):
        """
        验证返回状态码是否正确
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int( code ) == int( expected_code )
            return True
        except:
            self.log.error( f"code error,code is {code} ,expected code is {expected_code}" )
            raise
    def assert_body(self, body, expected_body):
        """
        验证返回结果内容是否正确
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert body == expected_body
            return True
        except:
            self.log.error( f"code error,body is {body} ,expected body is {expected_body}" )
            raise
    def assert_in_body(self, body, expected_body):
        """
        验证返回结果内容是否包含
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert expected_body in json.dumps(body)
            return True
        except:
            self.log.error( f"code error,body is {body} ,expected body is {expected_body}" )
            raise
