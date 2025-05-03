
my_list = []

def append1(x):
    my_list.append(x)
    print("Appended:", x)

def extend1(l):
    my_list.extend(l)
    print("Extended with:", l)

def pop():
    if my_list:
        print("Popped:", my_list.pop())
    else:
        print("List is empty")

def remove1(x):
    if x in my_list:
        my_list.remove(x)
        print("Removed:", x)
    else:
        print("Value not found in list")
