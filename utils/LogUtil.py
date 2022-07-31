import logging
import os
from datetime import datetime
from config import Conf
from config.Conf import ConfigYaml

__all__=["my_log"]

log_l={
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "critical": logging.CRITICAL
}


# 日志级别和扩展名需要在配置config中配置。
class Logger:
    def __init__(self, log_file, log_name, log_level):
        self.log_file=log_file
        self.log_name=log_name
        self.log_level=log_level

        self.logger=logging.getLogger( self.log_name )
        self.logger.setLevel( log_l[self.log_level] )

        if not self.logger.handlers:
            fh_stream=logging.StreamHandler()
            fh_file=logging.FileHandler( self.log_file, encoding="utf-8", mode="a" )
            formatter=logging.Formatter(
                '[%(levelname)s][%(process)d][%(thread)d]--%(asctime)s--[%(pathname)s %(funcName)s %(lineno)d]: %(message)s' )

            fh_stream.setLevel( log_l[self.log_level] )
            fh_file.setLevel( log_l[self.log_level] )

            fh_file.setFormatter( formatter )
            fh_stream.setFormatter( formatter )

            self.logger.addHandler( fh_stream )
            self.logger.addHandler( fh_file )


# 初始化日志路径
log_path=Conf.get_log_path()
current_time=datetime.now().strftime( "%Y-%m-%d" )
log_extension=ConfigYaml().get_conf_log_extension()
logfile=os.path.join( log_path, current_time + log_extension )
loglevel=ConfigYaml().get_conf_log()



def my_log(log_nmae=__file__):
    return Logger( log_file=logfile, log_name=log_nmae, log_level=loglevel ).logger


if __name__ == '__main__':
    my_log().debug( "aaaaaaaaaaaaaaaaaa")
