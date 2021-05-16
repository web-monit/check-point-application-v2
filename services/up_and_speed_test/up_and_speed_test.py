"""
    @author : Manouchehr Rasouli
"""
from urllib.request import urlopen
import time
from logger.logging import logger


def http_test(server_info):
    """
        this function will test the up status of the url
    :param server_info:
    :return:
    """
    try:
        start_time = time.time()
        data = urlopen(server_info).read()
        end_time = time.time()
        speed = end_time - start_time
        if type(data) is bytes:
            data = data.decode('utf-8')
        return {"status": True, "speed": speed, "data": data}
    except Exception as e:
        logger("EXCEPTION", "services/up_and_speed/http_test : " + str(e))
        return {'status': False, 'speed': -1, "data": -1}
