"""
    @author : Manouchehr Rasouli
"""
from config_loader import ConfigLoader
from logger.logging import logger
from message_broker_interface_sender import send_module


class ResultService:

    def __init__(self):
        """
        """
        loader = ConfigLoader()
        self.config = loader.get_config()
        self.sender = send_module.SendModule()

    def put_result(self, info):
        """
        :param info:
        :return:
        """
        # forward data into monitoring engine
        try:
            self.sender.send(destination=self.config["monit_engine.message_queue"]["result"], message=info)
            logger("INFO", "result_service/result_service/put_result : send test result for url_id " + info[
                "url_id"] + " into monitoring engine")
        except Exception as e:
            logger("EXCEPTION",
                   "result_service/result_service/put_result : exception on sending result for url_id " + info[
                       "url_id"] + " into monitoring engine : " + str(e))
