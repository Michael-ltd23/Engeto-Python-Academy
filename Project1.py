# PROJEKT_1
'''
author = Michael Černohorský
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
# USER INPUT + USERNAME AND PASSWORD VERIFICATION
USERS = dict(bob = '123', ann = 'pass123', mike = 'password123', liz = 'pass123')
SEPARATOR = 45 * '-'
USER_INPUT = input("Enter username: ")
PASSWD_INPUT = input("Enter passwd: ")
USER_LIST = [USER_INPUT, PASSWD_INPUT]

if USERS.get(USER_LIST[0]) == USER_LIST[1]:
    print(SEPARATOR)
    print(f"Welcome to the app, {USER_INPUT}")
    print(f"We have 3 texts to be analyzed.")
    print(SEPARATOR)
else:
    print(SEPARATOR)
    print("Incorrect username or password!")
    exit()

# TEXT SELECTION
TEXT_NUMBER = input("Choose text you want to analyse (1/2/3): ")
print(SEPARATOR)
if not TEXT_NUMBER.isdigit():
    print("Not number!")
    exit()
elif int(TEXT_NUMBER) not in range(1,4):
    print("Incorrect number!")
    exit()

# TEXT ANALYSES - TEXTS[TEXT_NUMBER]
TEXT_NUMBER = int(TEXT_NUMBER) - 1
TEXT_STRIP_LIST = []
START_UPPER_COUNT = 0
UPPER_COUNT = 0
LOWER_COUNT = 0
NUMBER_COUNT = 0
NUMBER_SUM = 0
# STRING SPLIT AND STRIP
WORD_SPLIT = TEXTS[TEXT_NUMBER].split(' ')
for word in WORD_SPLIT:
    TEXT_STRIP_LIST.append(word.strip('./,\n'))
# NUMBER OF 1) words 2) titlecase words 3) uppercase words 4) lowercase words 5) numeric strings 6) sum of all numbers
WORD_COUNT = len(TEXT_STRIP_LIST)
for word in TEXT_STRIP_LIST:
    if word[0].isupper():
        START_UPPER_COUNT += 1
    elif word.isupper():
        UPPER_COUNT += 1
    elif word.islower():
        LOWER_COUNT += 1
    elif word.isdigit():
        NUMBER_COUNT += 1
        NUMBER_SUM += int(word)
# WORD NUMBER
print(f'There are {WORD_COUNT} words in the selected text.')
# TITLECASE WORDS
print(f'There are {START_UPPER_COUNT} titlecase words.')
# UPPERCASE WORDS
print(f'There are {UPPER_COUNT} uppercase words.')
# LOWERCASE WORDS
print(f'There are {LOWER_COUNT} lowercase words.')
# NUMBERS
print(f'There are {NUMBER_COUNT} numeric strings.')
# SUM NUMBERS
print(f'The sum of all the numbers {NUMBER_SUM}.')
print(SEPARATOR)
print(f'LEN|    OCCURENCES  |NR.')
print(SEPARATOR)

# LENGTH OF WORDS - NUMBER OF OCCURRENCES
DICT_LENGTH = dict()
    # DICTIONARY = KEY - word_length, VALUES - number of occurences
for item in TEXT_STRIP_LIST:
    length = len(item)
    DICT_LENGTH[length] = DICT_LENGTH.setdefault(length, 0) + 1
# SORTED DICTIONARY
DICT_SORTED = dict(sorted(DICT_LENGTH.items()))
for i in DICT_SORTED:
    if i < 10:
        print(f"  {i}|{DICT_LENGTH[i] * '*'} |{DICT_LENGTH[i]}")
    else:
        print(f" {i}|{DICT_LENGTH[i] * '*'} |{DICT_LENGTH[i]}")
























