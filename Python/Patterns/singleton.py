class Singleton(object):
    """
    classic realisation of Singleton pattern
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


check = Singleton()
print("Object created", check)
check2 = Singleton()
print("Object created", check2)

if isinstance(check, Singleton) & isinstance(check2, Singleton):
    print(True)

if check == check2:
    print('It\'s the same!')
