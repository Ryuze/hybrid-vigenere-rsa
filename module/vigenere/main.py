import random
from ordered_set import OrderedSet

def originalTable():
    table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    return table
    
def scrambleTable(key):
    table = originalTable()
    
    unique_key = uniqueKey(key)
    
    random.Random(unique_key).shuffle(table)
    return table

def uniqueKey(key):
    unique_key = OrderedSet(list(key))
    return ''.join(unique_key)

# TODO: bawah ini cuma percobaan, tidak termasuk dalam ide
# table.insert(random.Random('a').randint(0, len(table)), 'key_per_huruf_disini')