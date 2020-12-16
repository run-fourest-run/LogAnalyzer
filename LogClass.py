import os
import re

file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'

class Log:

    __slots__ = ('version','phase')

    VERSION_PATTERN = re.compile(r'version\s[0-9]\.[0-9][0-9]\.[0-9]')
    PHASE_PATTERN = re.compile()

    def __init__(self, version,phase):
        self.__version = version
        self.__phase = phase

    @property
    def phase(self):
        return self.__phase

    @property
    def version(self):
        return self.__version




    @classmethod
    def from_file(cls,file):
        with open(file) as f:
            lines = f.readlines()
            version_object = next(filter(None, (re.search(cls.VERSION_PATTERN, x) for x in lines)))
            version = version_object.group()

            return cls(version)


    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r})'.format(classname,self.__version)




newloginstance = Log.from_file(file)
print(newloginstance)