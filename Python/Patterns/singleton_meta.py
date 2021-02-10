class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

            """или такой кусок кода 
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            """
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()

if isinstance(logger1, Logger) & isinstance(logger2, Logger):
    print(True)

if logger1 == logger2:
    print('It\'s the same!')

