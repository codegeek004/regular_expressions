import re


### Mobile Number

number = input("Entr mobile number: ")
#match = re.match('^(\+91){1}[6-9]\d{9}$', number)
"""
    -> starts with one +91
    -> one digit between 6 to 9
    -> any other 9 digits between 0 to 9
"""

#contact = re.match('^\+91[\-\s]?[6-9]\d{2}[\-\s]?\d{3}[\-\s]?\d{4}$', number)
contact = re.match(r'^\+91[\-\s]?[6-9]\d{4}[\-\s]?\d{5}$', number)
"""
    This accepts all numbers in format
    -> ^ --> start of string
    -> Starts with +91 
    -> [\-\s]? --> Atmost one Space or dash 
    -> [6-9] --> one digit between 6 to 9
    -> \d{4} --> next 3 digits
    -> [\-\s]? --> Atmost one Space or dash
    -> \d{5} --> last 4 digits
    -> $ --> End of string

"""
print(contact)
if contact !=  None:
    print("Mobile number is valid")
else:
    print("Mobile number invalid")


## Note - Always sanitize mobile number before inserting in database

# function to sanitize number

def normalize(contact):
    contact = re.sub(r'[\s\-]', '', contact)

    if contact.startwith('+91'):
        return contact
    elif re.fullmatch('[6-9]\d{9}', contact):
        return '+91' + contact  
    else:
        return contact



"""
    first character = smallcase a to k
    second character = digit divisible by 3
    length >= 2
"""
"""
string = input("Enter the string: ")
match = re.fullmatch(r"[a-k]{1}[0369][a-zA-Z0-9#]*", string)
print(match)
if match !=  None:
    print("String is valid")
else:
    print("Stringinvalid")
"""




