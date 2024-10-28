**This is the start of my notes on python**

* To get a list of all built in python methods use the code below
    dir(__builtins__) 

* To get all the keys from a dictionary
    dictionary_name.keys()
* To get all values from dictionary
    dictionary_name.values()


* Lists represent arrays of values that may change during the course of the program:
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]

* Dictionaries represent pairs of keys and values:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

* Keys/values of a dictionary can be extracted with:
phone_numbers.keys()
phone_numbers.values()

Tuples represent arrays of values that are not to be changed during the course of the program:
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

You can get a list of Python builtin functions using:
dir(__builtins__)

You can get the documentation of a Python data type using:
help(str)
help(str.replace)
help(dict.values)

isinstance(x,type) returns true or false based on if value x matches type

*Different ways to format strings*
def person_name(first_name):
    #message ='Hi {}'.format(first_name)
    #message = f'Hi {first_name}'
    message ='Hi %s' % first_name
    return message
print(person_name('Mary'))

*dictionaries*
* is a list of items that have one key and one value


code ex1.)
        input = 'How are you'
        input.startswith("how","are","you")


code ex.2)
        def greater(l1):
            return[i for i in l1 if i  > 0]
            
        temp = [-5, 3, -1, 101]
        print(greater(temp))

code ex.3)
        def zeros(list1):
            return [i if not isinstance(i, str) else 0 for i in list1]



file notes
You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()
You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")
You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")
You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()