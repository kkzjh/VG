import logging
from Tools.file_path import *

class DoLog:
    def my_log(self, msg, leavl):
        my_logger = logging.getLogger('python')# 定义日志收集器
        my_logger.setLevel('DEBUG')# 设定级别
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')# 日志格式
        # ch = logging.StreamHandler()# 创建输出渠道
        # ch.setLevel('DEBUG')# 设定级别
        # ch.setFormatter(formatter)
        txt = logging.FileHandler(test_log_path, encoding='UTF-8')
        txt.setLevel('DEBUG')
        txt.setFormatter(formatter)
        # my_logger.addHandler(ch)# 两者对接
        my_logger.addHandler(txt)

        # 收集日志
        if leavl == 'DEBUG':
            my_logger.debug(msg)
        elif leavl == 'INFO':
            my_logger.info(msg)
        elif leavl == 'WARNING':
            my_logger.warning(msg)
        elif leavl == 'ERROR':
            my_logger.error(msg)
        elif leavl == 'CRITICAL':
            my_logger.critical(msg)

        # my_logger.removeHandler(ch)
        my_logger.removeHandler(txt)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    my_log = DoLog()
    my_log.debug('678')