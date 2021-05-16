"""
    @author : Manouchehr Rasouli
    @data   : 19 March 2018
    @since  : 19 March 2018
"""
import logging


# todo send exception logs into sentry
def logger(level, message):
    FORMAT = '%(asctime)-15s %(level)s %(data)s %(message)-8s'
    logging.basicConfig(format=FORMAT)
    d = {'level': level, 'data': message}
    logger = logging.getLogger('monitoring_check_point')
    logger.warning('%s', ' ', extra=d)
