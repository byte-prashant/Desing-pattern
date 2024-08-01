from abc import abstractmethod
import logging
class loggerOperation:


    @abstractmethod
    def log(self):
        pass



class LoggerFactory:

    registry = {}
    __instance = None

    # using singleton class

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(LoggerFactory, cls).__new__(cls)

        return cls.__instance



    @classmethod
    def register(cls, loggger_name:str):


        def wrapper(logger_class:loggerOperation):
            if loggger_name in cls.registry:
                print('Executor already exists. Will replace it')
            cls.registry[loggger_name] = logger_class
            print("logger registered")
            return logger_class


        return wrapper



    @classmethod
    def get_logger(cls, logger_name:str, **kwargs):

        if logger_name in cls.registry:
            return cls.registry[logger_name]

        # executor = exec(**kwargs)
        # return executor


@LoggerFactory.register('InDB')
class InDBLog(loggerOperation):

    def log(self):
        print("log into db")


@LoggerFactory.register('InFile')
class InFileLog(loggerOperation):

    def log(self):
        print("logging into file")



in_db_log = LoggerFactory().get_logger('InFile')
print("kanpur", in_db_log, id(in_db_log))
in_db_log = LoggerFactory().get_logger('InFile')
print("kanpur", in_db_log, id(in_db_log))
print("both the ids are same so this the singlton class")
in_db_log().log()








