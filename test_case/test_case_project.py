import unittest
from Tools.http_request import HttpRequest
from Tools.get_data import GetData
from config.data import Data
from Tools.autonumber import AutoNumber
from Tools.do_log import DoLog
import warnings


class TestHttpRequest(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    # 登陆
    def test_login(self):
        DoLog().info('开始执行用例{}:{}'.format("test_login", "正常登陆"))
        url = Data().url
        data = {
            "api": "login@index",
            "data": {
                "username": "13522272526",
                "password": "123456"
            }
        }
        runner = HttpRequest().http_request(url, data, 'post')
        if runner.cookies:
            setattr(GetData, 'cookie', runner.cookies)
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))


    # 新增项目
    def test_1_addproject(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addproject", "新增项目{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "project@add",
    "data": {
        "user_id": 19,
        "name": "测试项目名称{}".format(AutoNumber.autonumber()),
        "expect_income": "10000",
        "expect_profit_margin": "0.55",
        "expect_public_time": 1648569600,
        "expect_pay_time": 1648569600,
        "demand": "无",
        "demand_att": "202203/a9d07548-5dfb-396e-7b70-f8ecafd39813.png",
        "resource_att": "",
        "is_rebate": 1,
        "is_serve": 1,
        "brand": "品牌",
        "is_matching": 10,
        "service_tariffing_rate": "0.5"
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 分配媒介
    def test_2_medium(self):
        DoLog().info('开始执行用例{}:{}'.format("test_medium", "分配媒介"))
        url = Data().url
        data = {
    "api": "project@medium",
    "data": {
        "project_id": "26",
        "department_id": 12,
        "medium_id": 2
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 接收任务
    def test_3_jieshourenwu(self):
            DoLog().info('开始执行用例{}:{}'.format("test_jieshourenwu", "接收任务"))
            url = Data().url
            data = {
    "api": "project@receiveMedium",
    "data": {
        "project_id": ""
    }
}
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 匹配资源
    def test_4_addprojectResource(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addprojectResource", "匹配资源"))
        url = Data().url
        data = {
    "api": "projectResource@add",
    "data": {
        "platform": 3,
        "resource_name": "我的微博爱抽风",
        "url": "https://weibo.com/u/6338469755",
        "position_id": "1",
        "supplier_id": 66,
        "resource_price": 11111,
        "execute_price": 11111,
        "execute_cost": 10111,
        "execute_gross_margin": 1.67,
        "user_price": 13333.2,
        "plan_public_time": 1648569600,
        "plan_pay_time": 1648569600,
        "bank_id": "",
        "invoice_type": "",
        "invoice_rate": "",
        "invoice_item": "",
        "rebate_base": 11111,
        "execute_rebate": "1000",
        "runtime_rebate": "2000",
        "runtime_cost": 10111,
        "runtime_gross_margin": 1.67,
        "plan_rebat_time": 1648569600,
        "rebate_invoice_type": "专票",
        "rebate_invoice_rate": "0.11",
        "rebate_invoice_item": "现代服务*推广服务费",
        "user_rebate": "3000",
        "user_bank_id": 8,
        "user_invoice_type": "形式发票",
        "user_invoice_rate": "0.22",
        "user_invoice_item": "其他咨询服务*咨询服务费",
        "is_prepaid": 2,
        "is_platform": 1,
        "is_supplier_rebate": 1,
        "is_user_rebate": 1,
        "project_id": 22,
        "resource_id": 101,
        "execute_gross_profit": 222.2,
        "runtime_gross_profit": 222.2,
        "final_cost": 10111,
        "final_gross_profit": 222.2,
        "final_gross_margin": 1.67,
        "final_rebate": "1000"
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))


    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()

