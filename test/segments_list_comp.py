import re
from itertools import chain,groupby


input_file = r'C:\Users\afournier\Desktop\testcopy3.log'
script_name_regex_pattern = r'^Manta\sFlow\s(\w*\s\w*\s\w*)\sScenario\s\(version\s[0-9]\.[0-9][0-9]\.[0-9]\)'
regex_pattern = re.compile(script_name_regex_pattern)
key_function = lambda line: re.search(regex_pattern,line)

segments_list = []
with open(input_file) as f:
    segments = groupby(f,key_function)
    segment_gen_exp = (chain([next(v)], (next(segments)[1])) for k, v in segments if k)
    segment_list_comp = [segment for segment in segment_gen_exp]
    for segment in segment_list_comp[0]:
        print(segment)





with open(input_file) as f:
    segments = groupby(f,key_function)
    segment_gen_exp = (chain([next(v)], (next(segments)[1])) for k, v in segments if k)
    segment_list_comp = [segment for segment in segment_gen_exp]
    for segment in segment_list_comp:
        print(segment)