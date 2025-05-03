my_dict = {}

def len3(d):
    print("Dictionary length:", len(d))

def add3(k, v):
    my_dict[k] = v
    print(f"Added ({k}: {v})")

def keys3():
    print("Keys:", list(my_dict.keys()))

def values3():
    print("Values:", list(my_dict.values()))
