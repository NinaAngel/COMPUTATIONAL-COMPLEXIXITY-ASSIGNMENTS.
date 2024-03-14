import re

test_string = input
char_rm = input

def white_strip(string, remove):
    if remove != '':
        strip_regex = re.compile(remove)
        new_string = strip_regex.sub('', string)
        return new_string
    else:
        strip_regex = re.compile('^\s*')
        new_string = strip_regex.sub('', string)
        strip_regex = re.compile('\s*$')
        new_string = strip_regex.sub('', new_string)
        return new_string


new_string = white_strip(test_string, char_rm)
print(new_string)




















