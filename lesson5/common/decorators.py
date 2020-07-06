from inspect import stack
import logging
from common.settings import LOGGING_LEVEL


def log(func):
    def call(*args, **kwargs):
        arg = list(args) + list(kwargs.items())
        print(stack()[1][3])
        # print(f'Функция < {func.__name__} > вызвана с аргументами {arg}')
        LOGGER = logging.getLogger(__name__)
        LOGGER.LOGGING_LEVEL(f'{stack()[1][3]}')
        return func(*args, **kwargs)

    return call


