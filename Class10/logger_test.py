import logging
from unittest import TestCase

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(
                    filename='logfile.log’, # set the output file
                    filemode='a’, # set it to append rather than overwrite
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s’, # determine the format of the output message
                    datefmt='%H:%M:%S’, # determine the format of the output time
                    level=logging.ERROR) # determine the minimum message level it will accept


class TestTranslatePage(TestCase):
    def test_001(self):
        logger.info('Logged INFO message')
        logger.warning('Logged WARNING message')
        logger.error('Logged ERROR message')
        assert 1 == 1
