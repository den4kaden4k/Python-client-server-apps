import logging
import os

path_log = os.path.join('log', 'messenger.log')
logging.basicConfig(
    filename=path_log,
    format='%(asctime)s %(levelname)s %(module)s %(message)s',
    level=logging.DEBUG
)

LOG = logging.getLogger(f'messenger.{__name__}')
