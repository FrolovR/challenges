# Solution by Roman Frolov
# Thanks to kurosawa4434
​
​
# this code cheks if a is in dictionary with key b and vice-versa
def Connected(a, b, dict):
    if a in dict[b]:
        return True
    elif b in dict[a]:
        return True
    else:
        return False
        
# recursion through dictionary until the end of Range
def RecursiveConnection(power, city0, connections, network, steps):
    for city in connections:
​
        if steps <= 0 and Connected(power, city, network) is False:
            continue
​
        elif Connected(power, city, network) is False:
            if RecursiveConnection(power, city0, network[city], network, steps - 1) is not None:
                return city0
​
        elif Connected(power, city, network) is True:
            return city0
​
    return None
        
def power_supply(networks, power_plants):
​
    # declaration of variables
    
    temp = list()
​
    # make network dictionary
​
    nw_dict = {}
​
    for n1, n2 in networks:
​
        if n1 not in nw_dict:
            nw_dict[n1] = []
​
        if n2 not in nw_dict:
            nw_dict[n2] = []
​
        nw_dict[n1].append(n2)
        nw_dict[n2].append(n1)
    
    # easy access to power plant and range
    
    number_of_plants = 0
    
    if bool(power_plants) == False:
        return set(nw_dict)
            
    for plant in power_plants:
        if 'p' in plant or 'c' in plant:
            number_of_plants += 1
            power = plant
            Range = power_plants[power]
        
        if Range == 1:
    
            # storing our temporary list to be returned
            
            for name in nw_dict:
                if Connected(power, name, nw_dict) == False and name not in power_plants:
                    temp.append(name)
            
        elif Range == 0:
            
            for city in nw_dict:
                if city == power:
                    continue
                else:
                    temp.append(city)
            
        else:
            
            result_recursion = list()
            for city in nw_dict:
                if city in power_plants:
                    continue
                elif Connected(power, city, nw_dict) == True:
                    result_recursion.append(city)
                if RecursiveConnection(power, city, nw_dict[city], nw_dict, Range - 2) != None:
                    result_recursion.append(RecursiveConnection(power, city, nw_dict[city], nw_dict, Range - 2))
                    
            for city in nw_dict:
                if city not in result_recursion and city not in power_plants:
                    temp.append(city)
                    
    if number_of_plants > 1:
        final_temp = list()
        for unique in temp:
            if temp.count(unique) == number_of_plants:
                final_temp.append(unique)
        temp = final_temp
    
            
    if temp != None:
        result = set(temp)
    else:
        result = set()
    print(result)
    return result
                    
if __name__ == '__main__':
    assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['c2']), 'one blackout'
    assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3']), 'two blackout'
    assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([]), 'no blackout'
    assert power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0}) == set(['c0', 'c2']), 'weak power-plant'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}) == set([]), 'cooperation'
    assert power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
                         ['c5', 'c6'], ['c5', 'p7']],
                        {'p1': 1, 'p7': 1}) == set(['c3', 'c4', 'c6']), 'complex cities 1'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
                         ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
                       ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
                       ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
                      {'p0': 1, 'p12': 4, 'p8': 1}) == set(['c6', 'c7']), 'complex cities 2'
    assert power_supply([['c1', 'c2'], ['c2', 'c3']], {}) == set(['c1', 'c2', 'c3']), 'no power plants'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}) == set(['c3']), 'circle'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}) == set([]), 'more than enough'
    assert power_supply([["c1","p1"],["p1","p2"]],{"c1":1}) 
    assert power_supply([["p1","c2"],["c2","c3"],["c3","c4"],["c4","p5"],["c6","c7"],["c7","c8"],["c8","c9"],["c9","c10"],["c11","c12"],["c12","c13"],["c13","c14"],["c14","c15"],["c16","c17"],["c17","c18"],["c18","c19"],["c19","c20"],["p21","c22"],["c22","c23"],["c23","c24"],["c24","p25"],["p1","c6"],["c2","c7"],["c3","c8"],["c4","c9"],["p5","c10"],["c6","c11"],["c7","c12"],["c8","c13"],["c9","c14"],["c10","c15"],["c11","c16"],["c12","c17"],["c13","c18"],["c14","c19"],["c15","c20"],["c16","p21"],["c17","c22"],["c18","c23"],["c19","c24"],["c20","p25"]],{"p25":3,"p1":3,"p21":3,"p5":3}) == set(['c13'])
    print("Looks like you know everything. It is time for 'Check'!")