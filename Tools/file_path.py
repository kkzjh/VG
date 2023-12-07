import os

file_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 配置文件路径
case_config_path = os.path.join(file_path, 'config', 'case.conf')

# 测试报告路径
test_report_path = os.path.join(file_path, 'test_result', 'html', 'test_api.html')

# log路径
test_log_path = os.path.join(file_path, 'test_result', 'log', 'log.txt')

# 测试自增
test_number_path = os.path.join(file_path, 'config', 'a.txt')
test_tcode_path = os.path.join(file_path, 'config', 'tcode.txt')

if __name__ == '__main__':
    print(test_number_path)