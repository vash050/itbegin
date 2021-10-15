import os
import sys

import logging
import logging.handlers

SERV_FORMAT = logging.Formatter('%(asctime)-30s %(levelname)-20s %(filename)-30s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'data_log/server.log')

LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='midnight')
LOG_FILE.setFormatter(SERV_FORMAT)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.info('Информация')
    LOGGER.debug('Отладка')