from word2number import w2n
import csv
words_numeric = set()
words_substituted = {}

# Load in data from txt files
with open('./data/numeric_words.csv', 'r') as file:
    for row in csv.reader(file):
        words_numeric.add(row[0])

with open('./data/substituted_words.csv', 'r') as file:
    for row in csv.reader(file):
        if len(row) == 2:
            words_substituted[row[0]] = row[1]

def parsestr(s):
    for key in d.keys():
        if key in s:
            if type(d[key]) == str:
                s = s.replace(key, d[key])
            else:
                s = s.replace(key, d[key](s))
    return s

def parsestr_numeric(s):
    words = s.split()
    if not words: return ''
    i = 0
    while i < len(words) and words[i] in words_numeric:
        i = i + 1
    # print('PARSING:', ' '.join(words[:i]))
    if i == 0:
        return words[0] + ' ' + parsestr_numeric(' '.join(words[1:]))
    s = str(w2n.word_to_num(' '.join(words[:i]))) + ' ' + parsestr_numeric(' '.join(words[i:]))
    return s

def parsestr_substitute(s):
    print(words_substituted)
    words = s.split()
    for i in range(len(words)):
        if words[i] in words_substituted:
            print('HIT')
            words[i] = words_substituted[words[i]]
    return ' '.join(words)

# d ={'equals' : '=','equal': '=', 'plus':'+', 'minus':'-', 'over' : '/', 'divided by':'/', 'greater than' : '>','less than':'<', 'percentage':'%', 'percent':'%', \
#     'multiplied' :'*', 'multiply':'*', 'multiplied by' :'*', 'multiply by':'*', 'sum of' : sum_of}

# s = 'seventy one plus three'
# new_s = parsestr(s)
# print(new_s)

def parsestr(s):
    for key in d.keys():
        if key in s:
            if type(d[key]) == str:
                s = s.replace(key, d[key])
            else:
                s = s.replace(key, d[key](s))
    return s


# s = 'seventy one plus three'
# new_s = parsestr(s)
# print(new_s)

print(parsestr_numeric('Your total is four thousand two hundred ninety one dollars sixty seven cents and one hundred seventeen unborn fetuses'))
print(parsestr_numeric(parsestr_substitute('one plus two minus three times four equals zero')))
print(parsestr_numeric(parsestr_substitute('I hate epsilon delta proofs')))
