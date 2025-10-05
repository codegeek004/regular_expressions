"""
    Quantifiers --> We can specify the number of occurences of the match

    - a = Exactly one a
    - a+ = Atleast one a
    - a* = zero or more a
    - a? = atmost one a
    - a{n} = n number of a
    - a{n, m} = minimum n number of a and maximum m number of a
    - ^x = checks whether target string starts with x or not. --> used in search()
    - x$ = checks whether target string ends with x or not
"""

import re

matcher = re.finditer('a{1,2}', 'aabaaabababbbbbaaba')

for match in matcher:
    print(f"start: {match.start()}, end: {match.end()}, group: {match.group()}")

"""
    output:
        start: 0, end: 2, group: aa
        start: 3, end: 5, group: aa
        start: 5, end: 6, group: a
        start: 7, end: 8, group: a
        start: 9, end: 10, group: a
        start: 15, end: 17, group: aa
        start: 18, end: 19, group: a
"""
