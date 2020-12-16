import os
import re
print(os.path.dirname(os.path.realpath(__file__)))

file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
version_pattern = re.compile(r'version\s[0-9]\.[0-9][0-9]\.[0-9]')




with open(file) as f:
    lines = f.readlines()
    version_object = next(filter(None,(re.search(version_pattern,x) for x in lines)))
    print(version_object.group())



