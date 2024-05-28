class SingletonDeclaration(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonDeclaration, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class Singleton(metaclass=SingletonDeclaration):
    pass
