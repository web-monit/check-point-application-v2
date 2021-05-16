"""
    @author : Manouchehr Rasouli

        this database created for store and load jobs from db
"""
from database_management_system import database_connection_pool
import config_loader


class JobStore:

    def __init__(self):
        """
        """
        loader = config_loader.ConfigLoader()
        self.config = loader.get_config()
        connection_pool = database_connection_pool.ConnectionPool()
        connection = connection_pool.get_connection(self.config)
        database = connection[self.config["check_point.data_base"]["database_name"]]
        self.collection = database[self.config["check_point.data_base"]["job_collection"]]

    def store_job(self, info):
        """
        :param info:
        :return:
        """
        self.collection.insert_one({'job': info})

    def get_jobs(self):
        """
        :return:
        """
        jobs = []
        for job in self.collection.find({}):
            if job['job']['is_valid'] == 'yes':
                jobs.append(job["job"])
        return jobs

    def delete_job(self, url_id):
        """
            delete the url from system
        :param url_dic:
        :return:
        """
        return self.collection.update({"job.url_id": str(url_id)}, {"$set": {"job.is_valid": "no"}})

    def update_job(self, info):
        """
        :param info:
        :return:
        """
        raise NotImplementedError
