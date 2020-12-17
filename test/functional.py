from itertools import groupby,chain

'''Attempting to first implement using a functional style of programming. Will attempt to refactor using a more reusable oop approach if 
that makes sense'''



'''
the delimiter is static in the previous example. In this example it needs to be dynamic. 

'''

delimiter = 'message'
input_file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
key_function = lambda line: line.lstrip().startswith(delimiter)



#gets the chunks of Data
def get_messages(input_file,key_function):
    with open(input_file) as f:
        groups = groupby(f,key_function)
        for k,v in groups:
            if k:
                yield chain([next(v)], (next(groups)[1]))


for x in get_messages(input_file,key_function):
    print(x)