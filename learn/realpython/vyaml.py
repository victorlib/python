# -*- coding:utf-8 -*-

import os
import logging.config
import yaml

def setup_logging(default_path='logging.yaml', default_level=logging.INFO):
    """
    Setup logging configuration
    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        print('the input path doesn\'t exist')


if '__main__' == __name__:
    setup_logging(default_path='logging.yaml')
    # default root logger
    logger = logging.getLogger()
    logging.info('jhaa', exc_info=True)
    logging.error('error', exc_info=False)



















































