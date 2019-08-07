print("imported  my_module...")

test = 'Test String'

def find_index(to_search, target): #find the index of value in a sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i

#if did find the value
    return -1