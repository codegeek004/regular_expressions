'''
    Predefined Character Classes
    
    - \s = space character
    - \S = any character except space
    - \d = any digit from 0-9
    - \D = any character except digit
    - \w = any word character [a-zA-Z0-9]
    - \W = any character except word(special characters)
    - . = any character including special characters
'''

import re

matcher = re.finditer('\W', 'skljsbgipsug 3    7$#^#^#@!@ksdjbgsjkbg')
for match in matcher:
    print(f"start: {match.start()}, end: {match.end()}, group: {match.group()}")

"""
    Output:
        start: 12, end: 13, group:  
        start: 14, end: 15, group:  
        start: 15, end: 16, group:  
        start: 16, end: 17, group:  
        start: 17, end: 18, group:  
        start: 19, end: 20, group: $
        start: 20, end: 21, group: #
        start: 21, end: 22, group: ^
        start: 22, end: 23, group: #
        start: 23, end: 24, group: ^
        start: 24, end: 25, group: #
        start: 25, end: 26, group: @
        start: 26, end: 27, group: !
        start: 27, end: 28, group: @ 
"""
