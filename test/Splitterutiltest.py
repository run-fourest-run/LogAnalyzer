import re
from itertools import chain,groupby





input_file = r'C:\Users\afournier\Desktop\testcopy3.log'
script_name_regex_pattern = r'^Manta\sFlow\s(\w*\s\w*\s\w*)\sScenario\s\(version\s[0-9]\.[0-9][0-9]\.[0-9]\)'
regex_pattern = re.compile(script_name_regex_pattern)
key_function = lambda line: re.search(regex_pattern,line)


def get_script_chunks(input_file,key_function):
    with open(input_file) as f:
        groups = groupby(f,key_function)
        for k,v in groups:
            if k:
                chunk = chain([next(v)], (next(groups)[1]))
                yield chunk

list_of_chunks = []
for chunk in get_script_chunks(input_file,key_function):
    list_of_chunks.append(chunk)
    for line in list_of_chunks[0]:
        print(line)
