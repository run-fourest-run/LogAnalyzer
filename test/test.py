from itertools import groupby,chain

# itertools - groupby : https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
# lambda functions: https://realpython.com/python-lambda/#python-lambda-and-regular-functions





input_file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
delimiter = ','
def key_function(line):
    line.lstrip().startswith(delimiter)
    return line




lambda_key_function = lambda line: line.lstrip().startswith(delimiter)




def get_messages(input_file,key_function):
    with open(input_file) as f:
        groups = groupby(f,key_function)
        for k,v in groups:
            print(v)
            if k:
                yield chain([next(v)], (next(groups)[1]))



testobject = get_messages(input_file,key_function)
for object in testobject:
    print(object)