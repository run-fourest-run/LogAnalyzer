import datetime
import re
from collections import deque

testfile = r'C:\Users\afournier\Desktop\48666_26_11_2020_14_33_14.log'
file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
DATE_PATTERN = re.compile('\d\d:\d\d:\d\d')



class Log:


    VERSION_PATTERN = re.compile(r'version\s[0-9]\.[0-9][0-9]\.[0-9]')
    SCRIPT_NAME_PATTERN = re.compile(r'Manta\sFlow\s(\w+)\s(\w+)')
    ANALYSIS_PHASE_NAME_PATTERN  = re.compile('Analyzer')
    EXRACTOR_PHASE_NAME_PATTERN = re.compile('Extractor')



    def __init__(self, version,script_name,phase,elapsedtime):
        self.__version = version
        self.__script_name = script_name
        self.__phase = phase
        self.elapsedtime = elapsedtime



    @property
    def version(self):
        return self.__version

    @property
    def scriptname(self):
        return self.__script_name
    def __iter__(self):
        return (i for i in (self.__version,self.__script_name,self.__phase,self.elapsedtime))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r},{!r},{!r})'.format(classname,self.__version,self.__script_name,self.__phase,self.elapsedtime)





    @classmethod
    def from_file(cls,file):
        with open(file) as f:
            lines = f.readlines()
            version_object = next(filter(None, (re.search(cls.VERSION_PATTERN, x) for x in lines)))
            version = version_object.group()

            script_name_object = next(filter(None, (re.search(cls.SCRIPT_NAME_PATTERN, x) for x in lines)))
            script_name = script_name_object.group()

            phase_extraction = re.search(cls.EXRACTOR_PHASE_NAME_PATTERN, script_name)
            phase_analysis = re.search(cls.ANALYSIS_PHASE_NAME_PATTERN, script_name)
            phase = ''
            if phase_extraction is not None:
                phase = 'extraction'
            elif phase_analysis is not None:
                phase = 'analysis'
            elif phase_analysis is None & phase_extraction is None:
                phase = 'unknown'

            start_date_object = next(filter(None, (re.match(DATE_PATTERN, x) for x in lines)))
            start_date_string = start_date_object.group(0)
            deque_end_date = deque(lines, maxlen=1)
            end_date_string = deque_end_date.pop()
            end_date_object = re.match(DATE_PATTERN, end_date_string)
            end_date_string = end_date_object.group(0)

            start_datetime_object = datetime.datetime.strptime(start_date_string, '%M:%S:%f')
            end_datetime_object = datetime.datetime.strptime(end_date_string, '%M:%S:%f')
            elapsed_time = end_datetime_object - start_datetime_object










            return cls(version,script_name,phase,elapsed_time)






newloginstance = Log.from_file(testfile)
for attributes in newloginstance:
    print(attributes)