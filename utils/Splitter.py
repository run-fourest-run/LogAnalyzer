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





















'''

for section in get_script_chunks(test_input_file,key_function):
    all_sections = []
    list_section = (list(section))
    all_sections.append(list_section)
    print(len(all_sections))

    begininng_line = list_section[2]
    print(begininng_line)


'''

'''
This works. It returns a regex object per match found. 
with open(test_input_file) as f:
    lines = f.readlines()
    for line in lines:
        regexobj = re.match(regex_pattern,line)
        if regexobj:
            print(regexobj)

'''







