"""
    @author : Manouchehr Rasouli
"""
from services import job
from scheduler import scheduler
from database_management_system import job_database
from logger.logging import logger


class UrlService:

    def __init__(self):
        """
        """
        self.database = job_database.JobStore()

    def add_url(self, info):
        """

            start scheduling the new url into the scheduler

        :param info:
        :return:
        """
        new_job = job.Job(info)
        job_scheduler = scheduler.Scheduler.get_scheduler()
        job_scheduler.add_job(function=new_job.do, kwargs=None,
                              minutes=info["credit"]["url_activities"]["check_time_slot"],
                              id=info["url_id"])
        # store the job info into the database
        self.database.store_job(info=info)

    def load_urls_to_scheduler(self):
        """
            this function will call at starting level of check point
        :return:
        """
        logger("INFO", "url_service/url_service/load_urls_to_scheduler : start loading jobs into scheduler")
        jobs = self.database.get_jobs()
        job_scheduler = scheduler.Scheduler.get_scheduler()
        for item in jobs:
            new_job = job.Job(item)
            job_scheduler.add_job(function=new_job.do, kwargs=None,
                                  minutes=item["credit"]["url_activities"]["check_time_slot"],
                                  id=item["url_id"])
        logger("INFO", "url_service/url_service/load_urls_to_scheduler : jobs loaded into scheduler")

    def delete_url(self, info):
        """

            info is a url_id and action dictionary

        :param info:
        :return:
        """
        logger("INFO", "url_service/url_service/delete_url : delete url request started")
        job_scheduler = scheduler.Scheduler.get_scheduler()
        self.database.delete_job(info['url_id'])
        job_scheduler.remove_job(info['url_id'])
        logger("INFO", "url_service/url_service/delete_url : url " + info['url_id'] + " deleted successfully")
