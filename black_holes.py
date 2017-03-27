import math

def areaOfIntersection(x0, y0, r0, x1, y1, r1):
    rr0 = r0 * r0
    rr1 = r1 * r1
    d = math.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))
 
    #  Circles do not overlap
    if d > r1 + r0:
       return 0

    # Circle1 is completely inside circle0
    elif d <= abs(r0 - r1) and r0 >= r1:
      #  Return area of circle1
      return math.pi * rr1

    # Circle0 is completely inside circle1
    elif d <= abs(r0 - r1) and r0 < r1:
      #  Return area of circle0
      return math.pi * rr0

    # Circles partially overlap
    else:
      phi = (math.acos((rr0 + (d * d) - rr1) / (2 * r0 * d))) * 2
      theta = (math.acos((rr1 + (d * d) - rr0) / (2 * r1 * d))) * 2
      area1 = 0.5 * theta * rr1 - 0.5 * rr1 * math.sin(theta)
      area2 = 0.5 * phi * rr0 - 0.5 * rr0 * math.sin(phi)

    # Return area of intersection
      return area1 + area2


def IntersectionIsBigEnough(a1, a2, ain):
    compare = ain / a1 * 100
    compare = round(compare)
    if compare >= 55:
        return True
    else:
        compare = ain / a2 * 100
        compare = round(compare)
        if compare >= 55:
            return True
        else:
            return False
        
def ComparisonOfAreas(a1, a2, c1, c2):
    if a1 - a2 >= 0.2 * a1:
        return c1
    elif a2 - a1 >= 0.2 * a2:
        return c2
    else: 
        # print("areas are the same")
        return None
        
def FindDistance(c1, c2):
        s1 = abs(c1[0] - c2[0])
        s2 = abs(c1[1] - c2[1])
        d = math.sqrt(s1**2 + s2**2)
        d = float("{0:.2f}".format(d))
        return d
    
    
def Absorption(area1, area2, big):
    new_area = area1 + area2
    new_radius = float("{0:.2f}".format(math.sqrt(new_area / math.pi)))
    circle = list()
    circle.append(big[0])
    circle.append(big[1])
    circle.append(new_radius)
    return circle

def checkio(data):
    
    data = list(data) # mutable list of input
    result = list(data) # result as a list
    eaten = list() # absorbed black holes 
    small = list() # list of distances between black holes
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            d = FindDistance(data[i], data[j])
            small.append(d)
            
    print(small)
    for i in small:
        if len(small) > 1:
            print(min(small))
            small[small.index(min(small))] = max(small)
            print(small)
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] in eaten or data[j] in eaten:
                continue
            
            # find distance between two centers of circles
            
            c1 = data[i]
            c2 = data[j]
            area1 = float("{0:.2f}".format(c1[2]**2 * math.pi))
            area2 = float("{0:.2f}".format(c2[2]**2 * math.pi))
            d = FindDistance(c1, c2)
            
            # calculate an area of intersection
            
            area = areaOfIntersection(c1[0], c1[1], c1[2], c2[0], c2[1], c2[2])
            area = float("{0:.2f}".format(area))
            if area == 0:
                # print("No intersection", data[i], data[j])
                continue
            
            # compare area of intersection to areas of two black holes
            
            compare = IntersectionIsBigEnough(area1, area2, area)
            if compare is False:
                continue
            
            # compare areas of two circles
            
            big = ComparisonOfAreas(area1, area2, c1, c2)
            # print(big, compare, c1, c2)
            if big is None:
                continue
            
            # absorption 
            
            pre = Absorption(area1, area2, big)
            
            if isinstance(data[0], list) is False:
                pre = tuple(pre)        
            
            if c1 in result and c2 in result:
                result[result.index(c1)] = pre
                result.remove(c2)
            else:
                result.append(pre)
                
            if big == data[i]:
                data[i] = pre
                eaten.append(data[j])
            elif big == data[j]:
                data[j] = pre
                eaten.append(data[j])
    
    print("result: ", result)
    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
    assert checkio([[3,3,3],[2,2,1],[6,3,2]]) == [[3,3,3.16],[6,3,2]]
    assert checkio([[0.8,0,1],[1,0,1],[1.5,0,0.5]]) == [[1,0,1.5]]