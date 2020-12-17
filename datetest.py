import re
import datetime
from collections import deque


file = r'C:\Users\afournier\Desktop\48666_26_11_2020_14_33_14.log'
example_date_string = '14:33:14 INFO  :0 - Main - Copyright (c) 2007-2019 Manta Tools.'
DATE_PATTERN = re.compile('\d\d:\d\d:\d\d')




with open(file) as f:
    lines = f.readlines()
    start_date_object = next(filter(None,(re.match(DATE_PATTERN,x) for x in lines)))
    start_date_string = start_date_object.group(0)
    deque_end_date = deque(lines, maxlen=1)
    print(deque_end_date)
    end_date_string = deque_end_date.pop()
    '''
    end_date_object = re.match(DATE_PATTERN,end_date_string)
    end_date_string = end_date_object.group(0)

    start_datetime_object = datetime.datetime.strptime(start_date_string, '%M:%S:%f')
    end_datetime_object = datetime.datetime.strptime(end_date_string,'%M:%S:%f')
    elapsed_time = end_datetime_object - start_datetime_object'''



