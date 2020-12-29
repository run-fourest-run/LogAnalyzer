from Log import Log
import re
from itertools import groupby,chain


class Segments:
    SCRIPT_NAME_PATTERN = r'^Manta\sFlow\s(\w*\s\w*\s\w*)\sScenario\s\(version\s[0-9]\.[0-9][0-9]\.[0-9]\)'

    def __init__(self,chunks):
        if chunks is None:
            self.chunks = []
        else:
            self.chunks = list(chunks)


    def __iter__(self):
        return (x for x in self.chunks)


    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r})'.format(classname,self.chunks)


    @classmethod
    def from_log(cls,log):
        lines = log.lines
        key_function = lambda line: re.search(cls.SCRIPT_NAME_PATTERN,line)
        segments = groupby(lines,key_function)
        chunks = [chain([next(v)], list(next(segments)[1])) for k, v in segments if k]

        return cls(chunks)

