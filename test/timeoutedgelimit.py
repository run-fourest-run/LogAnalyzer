import re

file = r'C:\Users\afournier\Desktop\48666_26_11_2020_14_33_14.log'
TIMEOUT_PATTERN = re.compile('')
EDGE_LIMIT_PATTERN = re.compile('')



with open(file) as f:
    lines = f.readlines()