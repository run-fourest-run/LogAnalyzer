import datetime
import re



class Log:

    #Class Attributes. These are just the regex patterns that are static

    VERSION_PATTERN = re.compile(r'version\s[0-9]\.[0-9][0-9]\.[0-9]')
    SCRIPT_NAME_PATTERN = re.compile(r'Manta\sFlow\s(\w+)\s(\w+)')
    ANALYSIS_PHASE_NAME_PATTERN  = re.compile('Analyzer')
    EXRACTOR_PHASE_NAME_PATTERN = re.compile('Extractor')
    DATE_PATTERN = re.compile('\d\d:\d\d:\d\d')




    def __init__(self,lines,version,script_name,phase,elapsedtime):
        if lines is None:
            self.lines = []
        else:
            self.lines = list(lines)
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

    @property
    def phase(self):
        return self.__phase






    #Magic Methods - str, repr, iter
    def __iter__(self):
        return (i for i in (self.__version,self.__script_name,self.__phase,self.elapsedtime))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r},{!r},{!r},{!r})'.format(classname,self.lines,self.__version,self.__script_name,self.__phase,self.elapsedtime)





    # Constructor to build the Log object from a file
    #example: logfile = LogFile.from_file(file)

    @classmethod
    def from_file(cls,file):
        with open(file) as f:
            lines = f.readlines()

            #version attribute logic
            version_object = next(filter(None, (re.search(cls.VERSION_PATTERN, x) for x in lines)),False)
            if version_object == False:
                version = 'unknown'
            else:
                version = version_object.group()


            #script_name_attribute_logic
            script_name_object = next(filter(None, (re.search(cls.SCRIPT_NAME_PATTERN, x) for x in lines)))
            script_name = script_name_object.group()



            #phase attribute logic - This needs to be revisited I don't think the logic is correct
            phase_extraction = re.search(cls.EXRACTOR_PHASE_NAME_PATTERN, script_name)
            phase_analysis = re.search(cls.ANALYSIS_PHASE_NAME_PATTERN, script_name)
            phase = ''
            if phase_extraction is not None:
                phase = 'Extraction'
            elif phase_analysis is not None:
                phase = 'Analysis'
            elif phase_analysis is None & phase_extraction is None:
                phase = 'Unknown'




            #execution time logic - Returns a datetime object
            start_date_object = next(filter(None, (re.match(cls.DATE_PATTERN, x) for x in lines)))
            start_date_string = start_date_object.group(0)

            all_date_objects = filter(None, (re.match(cls.DATE_PATTERN, x) for x in lines))
            lastdate_object = None
            for lastdate_object in all_date_objects:
                continue
            end_date_string = lastdate_object.group(0)
            start_datetime_object = datetime.datetime.strptime(start_date_string, '%H:%M:%S')
            end_datetime_object = datetime.datetime.strptime(end_date_string, '%H:%M:%S')
            elapsed_time = end_datetime_object - start_datetime_object






            return cls(lines,version,script_name,phase,elapsed_time)


