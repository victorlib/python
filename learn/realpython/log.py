# -*- coding:utf-8 -*-

import logging
'''logging.basicConfig(level=logging.DEBUG,
                    filename = 'app.log', 
                    filemode = 'w',
                    format='%(name)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')
'''
#logging.basicConfig(level = logging.DEBUG)
#logging.debug('This will get logged')
#
#logging.debug('This will get logged to a file')
#
#logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
#logging.warning('This is a warning')
#
#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
#logging.info('Admin logged in')
#
#logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
#logging.warning('Admin logged out')
#
#name = 'John'
#logging.error('%s raised an error', name)
#logging.error(f'{name} raised an error')
#
#a = 5
#b = 0
#
#try:
#    c = a / b
#except Exception as e:
#    logging.exception("Exception occurred")
#
#logger = logging.getLogger('example_logger')
#logger.warning('This is a warning')
#
#
# Create a custom logger
#logger = logging.getLogger(__name__)
#
## Create handlers
#c_handler = logging.StreamHandler()
#f_handler = logging.FileHandler('file.log')
#c_handler.setLevel(logging.WARNING)
#f_handler.setLevel(logging.ERROR)
#
## Create formatters and add it to handlers
#c_format = logging.Formatter('%(name)s - %(levelname)s -%(message)s')
#f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#c_handler.setFormatter(c_format)
#f_handler.setFormatter(f_format)
#
## Add handlers to the logger
#logger.addHandler(c_handler)
#logger.addHandler(f_handler)
#
#logger.warning('This is a warning')
#logger.error('This is an error')



import logging.config
import yaml
#
#logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
#
## Get the logger specified in the file
#logger = logging.getLogger(__name__)
#
#logger.error('This is a debug message')

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')























