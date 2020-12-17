from LogClass import Log

file_1 = r'C:\Users\afournier\Desktop\48666_26_11_2020_14_33_14.log'
file_2 = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
file_3 = r'C:\mantaflow-jbhunt-r30.1\cli\log\cobolDataflowMasterScenario_cobol.properties.log'



#trying to instantiate from a list of files...
files = []
files.append(file_1)
files.append(file_2)
for file in files:
    print(Log.from_file(file))

print(Log.from_file(file_3))

