my_set = set()

def slen2(s):
    print("Length of set:", len(s))

def adds2(x):
    my_set.add(x)
    print("Added to set:", x)

def remove2(x):
    if x in my_set:
        my_set.remove(x)
        print("Removed from set:", x)
    else:
        print("Element not found in set")
