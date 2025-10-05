"""
    Character classes

    Use the character classes to search a group of characters

    -> [abc] = either a or b or c
    -> [^abc] = except a and b and c
    -> [a-z] = any lower case
    -> [A-Z] = any upper case
    -> [a-zA-Z] = any alphabet
    -> [0-9] = Any digit from 0-9
    -> [a-zA-Z0-9] = any alphanumeric 
    -> [^a-zA-Z0-9] = except alphanumeric
"""

import re
matcher = re.finditer('[^a-zA-Z0-9]', 'l(&^LKNxZr*e$g!!34')

for i in matcher:
    print(f"start: {i.start()}, end: {i.end()}, group: {i.group()}")


"""
    Output:
        start: 1, end: 2, group: (
        start: 2, end: 3, group: &
        start: 3, end: 4, group: ^
        start: 10, end: 11, group: *
        start: 12, end: 13, group: $
        start: 14, end: 15, group: !
        start: 15, end: 16, group: !
"""


