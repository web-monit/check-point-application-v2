"""
    @author : Manouchehr Rasouli
"""
from logger.logging import logger
from logger.date_time import get_date
from services.up_and_speed_test import up_and_speed_test
from result_service import result_service
from config_loader import ConfigLoader


class Job:

    def __init__(self, job):
        """
        :param job: the job dictionary
        """
        self.job = job
        self.result_service = result_service.ResultService()
        loader = ConfigLoader()
        self.config = loader.get_config()

    def do(self):
        """
            the job that most scheduled
        :return:
        """
        logger("INFO", "services/job/do : start tests for job id " + self.job["url_id"])
        result = {
            "user_id": self.job["user_id"],
            "url_id": self.job["url_id"],
            "credit": self.job["credit"],
            "url_check_location": self.config["check_point.specification"]["location"],
            "time": get_date(),
            "result": {}
        }

        if self.job["credit"]["url_activities"]["up_check"]:
            result["result"]["up_and_speed"] = up_and_speed_test.http_test(self.job["url"])

        # todo implement other checks
        self.result_service.put_result(result)

        logger("INFO", "services/job/do : ent tests test interleave for job id " + self.job["url_id"])
