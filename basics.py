"""
    - compile() function compiles a pattern to RegexObject. It saves memory so it is used with finditer() or findall(). It generates an object which can be reused.    
        re.compile("aa")

    - finditer() function converts a pattern to iterable object. Iterable object creates an object once and needs to be iterated to access matched strings.
        match_pattern = re.finditer("aabbcc")

        We can call following methods after matching
        -> start() : Returns start index of match
        -> end() : Returns end index of match
        -> group() : Returns the matched string (item)

    - findall() function converts a pattern to a list of strings.
        re.findall("ab")
        Returns list ["abcd", "abd", "abde"]
"""

import re
string = 'abacabacba'
print(string)
#matcher = re.finditer('ab','abacabacba')
pattern = re.compile('ab')
matcher = pattern.finditer(string)
count = 0
for match in matcher:
    count+=1
    print(f"start = {match.start()}, end = {match.end()}, group = {match.group()}")
print(f"Total : {count}")

print()

pattern2 = re.compile('ba')
matcher = pattern2.finditer(string)
count = 0
for match in matcher:
    count+=1
    print(f"start = {match.start()}, end = {match.end()}, group = {match.group()}")
print(f"Total: {count}")



"""
    Output:
        abacabacba
        start = 0, end = 2, group = ab
        start = 4, end = 6, group = ab
        Total : 2

        start = 1, end = 3, group = ba
        start = 5, end = 7, group = ba
        start = 8, end = 10, group = ba
        Total: 3
"""
