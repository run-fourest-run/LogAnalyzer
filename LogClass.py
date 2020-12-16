import os
class Log:
    __slots__ = ('logname','phase','input_script')

    def __init__(self, license_expiration):




    @classmethod
    def from_file(cls,dir_path,*filename):
        if dir_path is None:
            dir_path = os.path.dirname(os.path.realpath(__file__) + '\\' + filename)
        with open(dir_path) as f:
            lines = f.readlines()






        return cls(messages,errors,warnings)


    def __repr__(self):
        classname = type(self).__name__
        return '{}({!},{!},{!},{!}'.format(classname,self.messages,self.errors,self.warnings)





print(os.path.dirname(os.path.realpath(__file__)))