import logging

# Set up logging configuration
logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

# Sample messages to be logged
logging.debug('Debugging message')
logging.info('Informational message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
