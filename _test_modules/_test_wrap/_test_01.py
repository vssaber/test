instances = {}


def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__
        print("=====1=====")
        if not cls_name in instances:
            print("====2====")
            instance = cls(args, **kw)
            instances[cls_name] = instance
        return instances[cls_name]
    return get_instance


@singleton
class User:
    _instance = None

    def __init__(self, name):
        print("====3====")
        self.name = name


u1 = User("pengjian")
u1.age = 20
u2 = User("pengjian2")
print(u2.age)
print(u1.name)
print(u1 is u2)


from functools import update_wrapper


WRAPPER_ASSIGNMENTS = {"__module__", "__name__", "__qualname__", "__doc__", "__annotations__"}


def wrapper(func):
    def inner_func():
        pass


    update_wrapper(inner_func, func)

    return inner_func

@wrapper
def wrapped():
    pass

print("dev2")

print(wrapped.__name__)