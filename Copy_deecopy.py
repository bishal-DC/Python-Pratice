#List is a reference id so it will be same as local and global variable to deal with this we have copy module
# string is a data copy which will be different as a local and global variable
import copy   # importing copy module

def eggs(parameter, string):

    print(f"DEBUG:Input in function list {parameter}")

    print(f"DEBUG:input in function string {string}")

    c = copy.deepcopy(parameter)  # copying the parameter list in a new variable

    c.append("Hello!")

    print(f"Inside function list output {c}")

    print(f"Inside function string output {string[:3]}")


spam = ['a', 'b', 'c', 'd', 'e']

name = 'Bishal Chakraborty'

eggs(spam, name)

print(f"outside function list output {spam}")

print(f"ouside function string output {name}")
