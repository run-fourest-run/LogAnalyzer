from itertools import groupby,chain

'''Attempting to first implement using a functional style of programming. Will attempt to refactor using a more reusable oop approach if 
that makes sense'''



delimiter = ''
input_file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\48666_26_11_2020_14_33_14.log'
key_function = lambda line: line.lstrip().startswith(delimiter)


#gets the chunks of Data
def get_messages(input_file,key_function):
    with open(input_file) as f:
        groups = groupby(f,key_function)
        for k,v in groups:
            if k:
                yield chain([next(v)], (next(groups)[1]))

get_messages()