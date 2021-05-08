import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')

file_handler = logging.FileHandler('Logs\wumbo.log')
file_handler.setFormatter(formatter)

log.addHandler(file_handler)

def debug(message):
    log.debug(message)

def info(message):
    log.info(message)

def warning(message):
    log.warning(message)

def error(message):
    log.error(message)

def critical(message):
    log.critical(message)

def exception(message):
    log.exception(message)
    




