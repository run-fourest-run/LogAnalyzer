import re

#input files. One does work one doesnt
file_dont_work = r'C:\Users\afournier\Desktop\48666_26_11_2020_14_33_14.log'
file_does_work = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'


#regex pattern
VERSION_PATTERN = re.compile(r'version\s[0-9]\.[0-9][0-9]\.[0-9]')



with open(file_dont_work) as f:
    lines = f.readlines()

    # version attribute logic
    version_object = next(filter(None, (re.search(VERSION_PATTERN, x) for x in lines)))
    print(version_object.group(0))
