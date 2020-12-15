class Log:
    __slots__ = ('logname','phase','input_script')

    def __init__(self, logname, phase, mantascript, messages):
        self.__logname = logname,
        self.phase = phase,
        self.mantascript = mantascript
        if messages is None:
            self.messages = []
        else:
            self.messages = list(messages)


    @property
    def logname(self):
        return self.__logname


    def __iter__(self):
        return ((a,b,c,d,e,f) for a,b,c,d,e,f in (self.logname,self.messages,self.errors,self.warnings,self.phase,self.input_script))

    def get_phase(self):
        pass

    def get_technology(self):
        pass


    def get_message(self,message):
        pass

    def get_warnings(self,warning):
        pass

    def get_errors(self,error):
        pass

    def get_execution_time(self):
        pass



    @classmethod
    def from_file(cls,filename):
        with open(filename) as f:
            warnings = ''
            messages = ''
            errors = ''

        return cls(messages,errors,warnings)


    def __repr__(self):
        classname = type(self).__name__
        return '{}({!},{!},{!},{!}'.format(classname,self.messages,self.errors,self.warnings)



