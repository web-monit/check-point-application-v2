"""
    @Author : Manouchehr Rasouli
    @Date   : 4/july/2018

    start to subscribing the check point into monitoring engine.

    subscription_message_dictionary = {
            "location": "config file",
            "host": "config file",
            "queue": "config file",
            "id": "config file"
        }


"""
from logger import logging, date_time
import config_loader
from message_broker_interface_sender import send_module


class Subscriber:

    def subscribe(self):
        """
            Start to subscribing the check point into main service
        :param connection:
        :param config_file:
        :return:
        """
        loader = config_loader.ConfigLoader()
        configuration = loader.get_config()

        # subscription message dictionary
        subscription_message_dictionary = {
            "type": "registry",
            "queue": configuration["check_point.message_server"]["subscription"],
            "id": configuration["check_point.message_server"]["id"],
            "time": date_time.get_date(),
            "location": configuration["check_point.specification"]["location"],
            "host": configuration["check_point.specification"]["host"]
        }

        # send data with sender module
        sender = send_module.SendModule()
        sender.send(destination=configuration["monit_engine.message_queue"]["registry"],
                    message=subscription_message_dictionary)
        logging.logger("INFO", "subscriber/check_point_subscriber : subscription is complete")
