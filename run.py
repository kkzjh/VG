import unittest
from Tools.file_path import *
from Tools import HTMLTestRunner
from test_case import test_case
from Tools import test_request


suite = unittest.TestSuite()
loader = unittest.TestLoader()

# 所有接口
# suite.addTest(loader.loadTestsFromModule(test_case))

# 登陆接口
suite.addTest(loader.loadTestsFromModule(test_request))

with open(test_report_path, 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="接口测试", description="暂无")
    runner.run(suite)