from Log import Log
from Segments import Segments
file_1 = r'C:\Users\afournier\Desktop\test.log'
file_2 = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
file_3 = r'C:\mantaflow-jbhunt-r30.1\cli\log\cobolDataflowMasterScenario_cobol.properties.log'
input_file = r'C:\Users\afournier\Desktop\testcopy3.log'



#trying to instantiate from a list of files...


log1 = Log.from_file(file_1)
sections = Segments.from_log(log1)



for section in sections.chunks[0]:
    print(section)




