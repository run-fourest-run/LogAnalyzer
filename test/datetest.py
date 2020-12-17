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

    all_date_objects = filter(None,(re.match(DATE_PATTERN,x) for x in lines))
    lastdate_object = None
    for lastdate_object in all_date_objects:
        continue
    end_date_string = lastdate_object.group(0)
    print(end_date_string)
    start_datetime_object = datetime.datetime.strptime(start_date_string, '%H:%M:%S')
    end_datetime_object = datetime.datetime.strptime(end_date_string,'%H:%M:%S')
    elapsed_time = end_datetime_object - start_datetime_object
    print(elapsed_time)



    '''
    end_date_object = re.match(DATE_PATTERN,end_date_string)
    end_date_string = end_date_object.group(0)

    start_datetime_object = datetime.datetime.strptime(start_date_string, '%M:%S:%f')
    end_datetime_object = datetime.datetime.strptime(end_date_string,'%M:%S:%f')
    elapsed_time = end_datetime_object - start_datetime_object'''



