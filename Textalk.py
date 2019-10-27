
def sum_of(s):

def parsestr(s):
    for key in d.keys():
        if key in s:
            if type(d[key]) == str:
                s = s.replace(key, d[key])
            else:
                s = s.replace(key, d[key](s))
    return s
d ={'equals' : '=','equal': '=', 'plus':'+', 'minus':'-', 'over' : '/', 'divided by':'/', 'greater than' : '>','less than':'<', 'percentage':'%', 'percent':'%', \
    'multiplied' :'*', 'multiply':'*', 'multiplied by' :'*', 'multiply by':'*', 'sum of' : sum_of}

s = 'sum of two and three.'
new_s = parsestr(s)
print(new_s)
