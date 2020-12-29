import re
from itertools import chain,groupby

script_name_regex_pattern = r'^Manta\sFlow\s(\w*\s\w*\s\w*)\sScenario\s\(version\s[0-9]\.[0-9][0-9]\.[0-9]\)'




input_file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
script_name_regex_pattern = r'\s(\w*\s\w*\s\w*)\sScenario\s\(version\s[0-9]\.[0-9][0-9]\.[0-9]\)'
regex_pattern = re.compile(script_name_regex_pattern)
key_function = lambda line: re.search(regex_pattern,line)


'''This works!!!!'''

with open(input_file) as f:
    segments = groupby(f,key_function)
    segment_list = [chain([next(v)], list(next(segments)[1])) for k, v in segments if k]
    for segment in segment_list[1]:
        print(segment)










'''
def get_file_data_chunks(*args):
    with open(input_file) as f:
        groups = groupby(f, key_function)
        for k, v in groups:
            if k:
                yield chain([next(v)], (next(groups)[1]))

def segments_list(*args):
    global_list = []
    for segment in get_file_data_chunks(input_file):
        segments = (list(segment))
        global_list.append(segments)
    return global_list

testlist = segments_list()
for x in testlist[3]:
    print(x)


'''




















'''
this also works... not sure why'''



'''

def get_file_data_chunks(*args):
    with open(input_file) as f:
        groups = groupby(f, key_function)
        for k, v in groups:
            if k:
                yield chain([next(v)], (next(groups)[1]))

def segments_list(*args):
    global_list = []
    for segment in get_file_data_chunks(input_file):
        segments = (list(segment))
        global_list.append(segments)
    return global_list

testlist = segments_list()
for x in testlist[2]:
    print(x)




'''




















'''
This kind of returns what I want...

There are three objects in the list which appears right. When I slice the segments_list by index 0 I am able to get the results I want. 


But any other index doesn't work. 
'''


with open(input_file) as f:
    segments = groupby(f,key_function)
    segment_list = [chain([next(v)], list(next(segments)[1])) for k, v in segments if k]
    for segment in segment_list[1]:
        print(segment)