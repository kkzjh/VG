import unittest
from Tools.http_request import HttpRequest
from Tools.get_data import GetData
from Tools.do_log import DoLog
import warnings
from test_case.test_case_login import test_data


class TestHttpRequest(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def test_api(self):
        for item in test_data:
            DoLog().info('开始执行用例{}:{}'.format(item["test_code"], item["title"]))
            runner = HttpRequest().http_request(item["url"], item["data"], item["http_method"])
            if runner.cookies:
                setattr(GetData, 'cookie', runner.cookies)
            try:
                self.assertEqual(item["expected"], runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))


    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
    print(TestHttpRequest().test_api())
