"""
    Important functions of re module
    
    - match() = matches the function to check the given pattern at the beginning of the target string. If it matches it returns the string or returns None

    - fullmatch() = matches the function to check the full string. Returns None if not found.

    - search() = searches in the string

    - findall() = find all occurences and store it in a list

    - finditer() = find all occurence and store it in a iterable object

    - sub() = substitutes characters with new characters 

    - subn() = substitutes characters with new characters and returns number of substitutions

    - split() = converts into a list 

    - compile() = it makes a reusable regex and does not. All other methods compile and execute the regex once you call them. Its faster when reused many times compared to other methods.

#### Note --> Always use r'' (raw strings) to avoid treating python '\' as escape character

"""

import re


# match() 
match = re.match('hello', 'hello world')
if match is not None:
    print('Match found')
else:
    print("Match not found")


# fullmatch()
full_match = re.fullmatch('hello world', 'hello')
if full_match is not None:
    print('full match found')
else:
    print("full match not found")


# search()
search_str = re.search('is', 'Indore is the cleanest city')
if search_str is not None:
    print('Match found')
else:
    print('Match not found')


#findall()
all_matches = re.findall('[0-9]', '2ace4$2nlf42kj')
print(all_matches)


#finditer()
matcher = re.finditer(r'\D', 'a55afdpS53')
for match in matcher:
    print(f"start index: {match.start()}, end index: {match.end()}, group: {match.group()}")


string = r"There are 25 oranges and 19 apples in the basket"

#sub()
sub_str = re.sub(r'\d', '#', string)
print(sub_str)


#subn()
subn_str = re.subn(r'\d', '#', string)
print(subn_str, type(subn_str))


#split()
split_str = re.split(r'\s', string)
print(split_str, type(split_str))

"""
    Output:
        Match found
        full match not found
        Match found
        ['2', '4', '2', '4', '2']
        start index: 0, end index: 1, group: a
        start index: 3, end index: 4, group: a
        start index: 4, end index: 5, group: f
        start index: 5, end index: 6, group: d
        start index: 6, end index: 7, group: p
        start index: 7, end index: 8, group: S
        There are ## oranges and ## apples in the basket
        ('There are ## oranges and ## apples in the basket', 4) <class 'tuple'>
        ['There', 'are', '25', 'oranges', 'and', '19', 'apples', 'in', 'the', 'basket'] <class 'list'>
"""
