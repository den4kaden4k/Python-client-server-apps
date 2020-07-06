from inspect import stack
from common.settings import LOGGING_LEVEL


def log(logger):
    def wrap(func):
        def call(*args, **kwargs):
            arg = list(args) + list(kwargs.items())
            message = f'Функция < {func.__name__} > вызвана из функции < {stack()[1][3]} > с аргументами {arg}'
            logger.debug(message)

            return func(*args, **kwargs)

        return call

    return wrap
