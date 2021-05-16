"""
    @author : Manouchehr Rasouli
"""
from schema import validator
import config_loader
from logger.logging import logger
from url_service import url_service


class Handler:

    def __init__(self):
        """
        """
        loader = config_loader.ConfigLoader()
        self.config = loader.get_config()
        self.validator = validator.SchemaValidator(schema_path=self.config["schema"]["handler_schema"])
        self.url_service = url_service.UrlService()

    def handle(self, info):
        """
        :param info:
        :return:
        """
        self.validator.check(info)
        logger("INFO", "message_handler/handler/handle : receive an action")
        if info["action"] == "add":
            self.url_service.add_url(info=info)
        elif info["action"] == "delete":
            self.url_service.delete_url(info=info)
        else:
            raise Exception("action " + info["action"] + " not implemented")
