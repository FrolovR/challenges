# solution by Roman Frolov

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.name = "Building"
        self.south = south # y = 0
        self.west = west # x = 0
        self.width_WE = width_WE # x axis
        self.width_NS = width_NS # y axis
        self.height = height

    def corners(self):
        # calculate coordinates of north-east and store it in list
        ne = list()
        ne.append(self.south + self.width_NS)
        ne.append(self.west + self.width_WE)
        # calculate coordinates of south-east and store it in list
        se = list()
        se.append(self.south)
        se.append(self.west + self.width_WE)
        # calculate coordinates of south-west and store it in list
        sw = list()
        sw.append(self.south)
        sw.append(self.west)
        # calculate coordinates of north-west and store it in list
        nw = list()
        nw.append(self.south + self.width_NS)
        nw.append(self.west)
        # update dictionary with coordinates of corners
        corners = {"north-east" : ne, "south-east" : se, "south-west" : sw, "north-west" : nw}
        return corners
        
    def area(self):
        # side * side
        return self.width_WE * self.width_NS

    def volume(self):
        # side * side * height
        return self.width_WE * self.width_NS * self.height

    def __repr__(self):
        # string representation of the building
        return '{name}({south}, {west}, {width_WE}, {width_NS}, {height})'.format(**self.__dict__)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
