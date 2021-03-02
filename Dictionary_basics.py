import pprint
message ='BBishal' # is learning phython and he is doing good so far

count={}

for letter in message:
    print(f"DEBUG:-The letter in the loop is {letter}")
    count.setdefault(letter,0)
    print(f"The actually executed part {count.setdefault(letter,0)}")
    print(f"DEBUG:- The dictionary after default check {count}")
    count[letter]=count[letter]+1
    print(f"DEBUG the output is after a loop {count}")

pprint.pformat(count)

