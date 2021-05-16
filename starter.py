"""
    @author : Manouchehr Rasouli
"""
import time
import config_loader
from message_broker_interface import connection, connection_handler
from message_broker_interface_listener import listener
from subscribe.check_point_subscriber import Subscriber
from url_service import url_service


def main():
    loader = config_loader.ConfigLoader()
    config = loader.get_config()
    connector = connection.Connection()
    general_connection = connector.get_connection()
    connection_handler.Handler(connection=general_connection,
                               connection_listener=listener,
                               topic=config["check_point.message_server"]["subscription"])
    # subscribe the check point into monitoring engine
    Subscriber().subscribe()
    # load jobs into scheduler
    url_service.UrlService().load_urls_to_scheduler()
    # run the application for ever
    keep_alive()


def keep_alive():
    """
        run for ever
    :return:
    """
    while True:
        time.sleep(10)


if __name__ == '__main__':
    main()
