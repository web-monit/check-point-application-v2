"""
    @Author : Manouchehr Rasouli
    @Date   : 28/June/2018
"""
import stomp
import config_loader
from logger.logging import logger


class Connection:

    def __init__(self):
        pass

    def get_connection(self):
        """
        Create and return a stomp connection into
        wanted host message broker.
        :return:
        """
        loader = config_loader.ConfigLoader()
        configuration = loader.get_config()

        logger("INFO", "message_broker_interface/connection : start to connecting to JMS")

        logger("INFO", "message_broker_interface/connection : jms server host : " +
               configuration["check_point.message_server"]["host"])

        logger("INFO", "message_broker_interface/connection : jms server port : " +
               str(configuration["check_point.message_server"]["port"]))

        connection = stomp.Connection([(configuration["check_point.message_server"]["host"],
                                        configuration["check_point.message_server"]["port"])])
        connection.start()

        connection.connect(configuration["check_point.message_server"]["user_name"],
                           configuration["check_point.message_server"]["password"],
                           wait=True)

        return connection
