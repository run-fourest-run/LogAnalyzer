from Log import Log



class Script:
    SCRIPT_NAME_PATTERN = r'^Manta\sFlow\s(\w*\s\w*\s\w*)\sScenario\s\(version\s[0-9]\.[0-9][0-9]\.[0-9]\)'

    def __init__(self,lines):
        if lines is None:
            self.lines = []
        else:
            self.lines = list(lines)





    @classmethod
    def from_log(cls,file):
        parent_object = Log.from_file(file)
        lines = parent_object.lines
        print(lines)
        return cls(lines)


