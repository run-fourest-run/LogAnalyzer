import os
import re
print(os.path.dirname(os.path.realpath(__file__)))

f = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
pattern = re.compile('version')


def license_key_search(pattern,filename):
    license_key_matches = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(pattern,line)
            if match:
                license_key_matches.append(line)
    return license_key_matches


