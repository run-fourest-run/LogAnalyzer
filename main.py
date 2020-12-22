from Log import Log

file_1 = r'C:\Users\afournier\Desktop\48666_26_11_2020_14_33_14.log'
file_2 = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
file_3 = r'C:\mantaflow-jbhunt-r30.1\cli\log\cobolDataflowMasterScenario_cobol.properties.log'
input_file = r'C:\Users\afournier\Desktop\testcopy3.log'



#trying to instantiate from a list of files...


log1 = Log.from_file(file_2)


print(log1.lines)