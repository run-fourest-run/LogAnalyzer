'''
The thought here is to have three custom classes - LogFile,Messages & Thread
these will be constructed from the .log file. They will have methods that will fetch information,
They should also be iterable(?)
'''




class LogFile:
    def __init__(self):
        self.filename = filename
        self.sourcesystem = sourcesystem
        self.phase = phase
        self.messages = messages


    def get_execution_time(self):
        pass

    def get_chunks(self):