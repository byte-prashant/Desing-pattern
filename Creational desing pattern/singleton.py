# The __init__ Constructor: In Python, __init__ is known as the constructor method. It’s called when an instance of a
# class is created. The primary purpose of __init__ is to initialize the attributes and properties of the object.
# It’s like the “setup” or “initialization” method for an object.
#
# The __new__ Constructor: The __new__ method is responsible for creating a new instance of a class. In Python,
# objects are created with the __new__ method before they are initialized with the __init__ method. It’s used when
# you want to customize object creation and is less commonly employed than __init__.


class Singleton:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls)

        return cls.__instance




# thread safe

import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # to make sure if another thread have not created the instance while aquiring lock
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
