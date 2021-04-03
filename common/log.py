import logging
import time

from common import dir_config


class MyLog:
    def loging(self, msg, level):
        # 日志收集器
        my_logging = logging.getLogger("zqh_log")

        # 设置级别
        my_logging.setLevel("DEBUG")
        log_format = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')

        # 创建输出渠道
        handler = logging.StreamHandler()
        handler.setLevel("DEBUG")
        handler.setFormatter(log_format)

        # 输出到文件及指定格式
        shot_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        file_handler = logging.FileHandler(dir_config.log_path + "{0}_log.txt".format(shot_time), encoding="utf-8")
        file_handler.setLevel("DEBUG")
        file_handler.setFormatter(log_format)

        # 进行对接
        my_logging.addHandler(handler)
        my_logging.addHandler(file_handler)

        if level == "DEBUG":
            my_logging.debug(msg)
        elif level == "INFO":
            my_logging.info(msg)
        elif level == "WARING":
            my_logging.warning(msg)
        elif level == "ERROR":
            my_logging.error(msg)
        elif level == "CRITICAL":
            my_logging.critical(msg)

        # 关闭渠道
        my_logging.removeHandler(handler)
        my_logging.removeHandler(file_handler)
