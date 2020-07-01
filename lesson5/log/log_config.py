import logging

logging.basicConfig(
    filename='log/messenger.log',
    format='%(asctime)s %(levelname)s %(module)s %(message)s',
    level=logging.DEBUG
)

LOG = logging.getLogger(f'messenger.{__name__}')
