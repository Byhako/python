import logging

logging.basicConfig(filename='report.log', level=logging.DEBUG)

logging.debug('Mi debug')
logging.info('Informacion')
logging.warning('Ten cuidado!')
logging.error('Eres un tonto.')
logging.critical('Error critico')