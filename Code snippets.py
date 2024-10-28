#To get user input
user_input = type(input("message to user:"))# type can = int, float, str


#inserts user input for %s
user_input("enter your name: ")
message = f"hello %s" % {user_input} # older python version (2 and below)
message = f"hello {user_input}" #newer python versions


name = "John"
surname = "Smith"
message = "Your name is {}. Your surname is {}".format(name, surname)



def person_name(first_name):
    message ='Hi {}'.format(first_name)
    message = f'Hi {first_name}'
    message ='Hi %s' % first_name
    return message
    
print(person_name(first_name=input('What is your first name: ')))

