def FindCommon(order, suborder):
    common = list()
    for char in suborder:
        if char in order:
            common.append(char)
    return common
    
def InsertBefore(char, insertion, order):
    i = order.index(char) 
    order[i:i] = insertion
    return order
    
def InsertBetween(a, b, insertion, order):
    i = order.index(a) + 1
    order[i:i] = insertion
    return order
    
def InsertAfter(char, insertion, order):
    i = order.index(char) + 1
    order[i:i] = insertion
    return order

def checkio(data):
    order = list() # alphabetical order in list
    
    # read first string
    for char in data[0]:
        if char not in order:
            order.append(char)  
    
    # iterate through input strings]
    for string in data:
        if string == data[0]:
            continue
        
        before = list()
        between = list()
        after = list()
        
        suborder = list()
        
        for char in string:
            suborder.append(char)
            
        common = FindCommon(order, suborder)
        
        if len(common) == 1:
            if string.index(common[0]) == 0:
                for char in string:
                    if char == common[0]:
                        continue
                    else:
                        after.append(char)
                order = InsertAfter(common[0], after, order)
            elif string.index(common[0]) == len(string) - 1:
                for char in string:
                    if char == common[0]:
                        continue
                    else:
                        before.append(char)
                order = InsertBefore(common[0], before, order)
        elif len(common) == 2:
            temp = list()
            for char in string:
                if char in common:
                    continue
                else:
                    temp.append(char)
            order = InsertBetween(common[0], common[1], temp, order)
        elif len(common) == 0:
            order.append(string)
                
    # stringify result list
    string = ""
    for char in order:
        string += char
    print(string)
    return string

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
    assert checkio(["hello","low","lino","itttnosw"]) == "helitnosw"
