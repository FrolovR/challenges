# solution by Roman Frolov 2017

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
    
def UnderstandableOrder(order, data):
    for string in data:
        if string == data[0]:
            continue
        if len(FindCommon(order, string)) >= 1:
            return True
    return False

def FinalCheck(order, data):
    temp = order    
    for i in range(len(order)):
        prevchar = list()
        char = None
        nextchar = list()
        
        # readability { chars before i } { i } { chars after i }
        for j in order:
            if order.index(j) < i:
                prevchar.append(j)
            elif order.index(j) == i:
                char = order[i]
            elif order.index(j) > i:
                nextchar.append(j)
        for string in data:
            # char is not in string
            if char not in string:
                continue
            
            # prevchars are not in string
            if prevchar:
                greatest = None
                # find greatest index of previous character
                for prev in prevchar:
                    if prev in string:
                        if greatest is None:
                            greatest = prev
                        if string.index(prev) > string.index(greatest):
                            greatest = prev
                # replace character in the right position after list prevchar
                if greatest is not None:            
                    if string.index(greatest) > string.index(char):
                        temp.remove(char)
                        temp = InsertBefore(greatest, char, temp)
                           
                            
            # nextchars are not in string
            if nextchar:
                least = None
                for nexty in nextchar:
                    if nexty in string:
                        if least is None:
                            least = nexty
                        if string.index(nexty) < string.index(least):
                            least = nexty
                # replace character in the right position before list nextchar
                if least is not None:
                    if string.index(least) < string.index(char):
                        temp.remove(char)
                        temp = InsertAfter(least, char, temp)
    
    temp = FindAmbiguous(temp, data)
    return temp

def FindAmbiguous(order, data):
    n1 = None # letter before
    n2 = None # letter after
    a = None # first ambiguous letter
    b = None # second ambiguous letter
    temp = order
    # case when 2 chars are in conflict; their neighbours are the same
    for string in data:
        for i in range(len(string)-1):
            if i is 0:
                continue
            elif i == len(string)-1:
                continue
            else:
                n1 = string[i-1]
                a = string[i]
                n2 = string[i+1]
                # now compare this variables to another strings
                for s in data:
                    if s == string:
                        continue
                    if n1 in s and n2 in s:
                        if s.index(n2) - s.index(n1) == 2:
                            b = s[s.index(n1)+1]
                            # case when this letters are in same string somewhere so we can determine the order
                            if TwoInOne(a, b, data):
                                continue
                            # we can not determine the order and hence sorting using alphabetical order
                            sort = list()
                            sort.append(a)
                            sort.append(b)
                            sort = sorted(sort)
                            c = sort[0]
                            d = sort[1]
                            inc = temp.index(c) 
                            ind = temp.index(d)
                            if inc > ind:
                                temp[ind] = c
                                temp[inc] = d
    return temp
   
def TwoInOne(a, b, data):
    for string in data:
        if a in string and b in string:
            return True
    return False

def checkio(data):
    order = list() # alphabetical order in list
    can_determine = False
    
    # read first string
    for char in data[0]:
        if char not in order:
            order.append(char)  
    
    if len(data) > 1:
        can_determine = UnderstandableOrder(order, data)
    else:
        can_determine = True
        
    # iterate through input strings
    for string in data:
        if string == data[0]:
            continue
        
        before = list()
        between = list()
        after = list()
        
        common = FindCommon(order, string)
        
        # only one common character
        if len(common) == 1:
            for char in string:
                if char in common:
                    continue
                elif string.index(char) < string.index(common[0]):
                    before.append(char)
                elif string.index(char) > string.index(common[0]):
                    after.append(char)
            order = InsertBefore(common[0], before, order)
            order = InsertAfter(common[0], after, order)
        # case with 2 common characters
        elif len(common) == 2:
            for char in string:
                if char in common:
                    continue
                elif string.index(char) < string.index(common[0]):
                    before.append(char)
                elif string.index(char) > string.index(common[0]) and string.index(char) < string.index(common[1]):
                    between.append(char)
                elif string.index(char) > string.index(common[1]):
                    after.append(char)
            order = InsertBefore(common[0], before, order)
            order = InsertBetween(common[0], common[1], between, order)
            order = InsertAfter(common[1], after, order)
        # case with more than 2 common characters
        elif len(common) > 2:
            temp = list()
            string = ''.join(sorted(set(string), key=string.index))
            for char in string:
                if char in common:
                    continue
                elif string.index(char) < string.index(common[0]):
                    before.append(char)
                elif string.index(char) > string.index(common[0]) and string.index(char) < string.index(common[-1]):
                    for i in range(len(common) - 1):
                        if string.index(char) > string.index(common[i]) and string.index(char) < string.index(common[i+1]):
                            temp.append(char)
                            if string.index(common[i+1]) == string.index(char) + 1:
                                order = InsertBetween(common[i], common[i+1], temp, order)
                                temp = list()
                elif string.index(char) > string.index(common[-1]):
                    after.append(char)
            order = InsertBefore(common[0], before, order)
            order = InsertAfter(common[-1], after, order)
        # if there is no common character
        elif len(common) == 0:
            for char in string:
                order.append(char)
         
    # filter order to make sure there is no duplicate characters
    temp = list()
    for char in order:
        if char in temp:
            continue
        temp.append(char)
    order = temp
    
    # if order is not determinable then sort order; otherwise make final sanity check
    if can_determine == False:
        order = sorted(order)
    else:
        order = FinalCheck(order, data)
        
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
    assert checkio(["my","name","myke"]) == "namyke"
    assert checkio(["xxxyyz","yyww","wwtt","ttzz"]) == "xywtz"
    assert checkio(["axton","bxton"]) == "abxton"
    assert checkio(["is","not","abc","nots","iabcn"]) == "iabcnots"
    assert checkio(["b","d","a"]) == "abd"
    assert checkio(["jhgfdba","jihcba","jigedca"]) == "jihgefdcba"
    assert checkio(["jhgedba","jihcba","jigfdca"]) == "jihgefdcba"