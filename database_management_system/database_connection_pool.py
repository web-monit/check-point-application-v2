"""
    @Author : Manouchehr Rasouli
    @Date   : 5/july/2018
"""
from pymongo import MongoClient
from logger.logging import logger


class ConnectionPool:

    def __inti__(self):
        """

        :return:
        """
        logger("INFO", "database_management_system/database_connection_pool : connection pool initialized")

    def get_connection(self, configuration):
        """
            this method will return a built in connection pool into mongodb database service
        :return:
        """
        return MongoClient(configuration["check_point.data_base"]["database_host"],
                           configuration["check_point.data_base"]["database_port"],
                           maxPoolSize=configuration["check_point.data_base"]["maximum_pool_size"],
                           waitQueueMultiple=configuration["check_point.data_base"]["wait_queue_time_out"])
