"""
    @Author : Manouchehr Rasouli
    @Date   : 5/july/2018


    this module created for manage and generate correct date and time
"""
from time import gmtime, strftime
import config_loader


def get_date():
    """
        generate and return the date
    :return:
    """
    loader = config_loader.ConfigLoader()
    configuration = loader.get_config()

    return strftime("%a, %d %b %Y %H:%M:%S " + str(configuration["check_point.specification"]["time_region"]),
                    gmtime())
