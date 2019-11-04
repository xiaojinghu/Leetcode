class PathCalculator:
    
    # You may enter code here.
    def __init__(self):
        # dist stores the distance from departure city to destination
        self.dist = {}
        # departToDest maps the departure city to a list of its destination
        self.departToDest = {}
    
    def process(self, line):
        
        # You must enter code here.
        # parse the info
        depart, dest, dist = line.split(":")
        dist = int(dist)
        # first add the info to our database
        self.dist[(depart, dest)] = dist
        self.dist[(dest, depart)] = dist
        if depart not in self.departToDest:
            self.departToDest[depart] = []
        self.departToDest[depart].append(dest)
        if dest not in self.departToDest:
            self.departToDest[dest] = []
        self.departToDest[dest].append(depart)
        
        maxDist = 0
        maxCity = ""
        flag1 = False
        flag2 = False
        
        # cehck if there is a X_DEPART_DEST pattern
        for city in self.departToDest[depart]:
            if city!=dest and self.dist[(city, depart)]>maxDist:
                maxDist = self.dist[(city, depart)]
                maxCity = city
                flag1 = True
        
        # check if there is a DEPART_DEST_X pattern
        for city in self.departToDest[dest]:
            if city!=depart and self.dist[(dest, city)]>maxDist:
                maxDist = self.dist[(dest, city)]
                maxCity = city
                flag2 = True
        # print(maxDist, maxCity)  
        if flag2:
            # it means the intemediate city is dest, we need to put it in the middle
            cities = [depart, maxCity]
            cities.sort()
            return str(maxDist+dist)+":"+cities[0]+":"+dest+":"+cities[1]
        if flag1:
            # it means the intermediate city is depart, we need to put it in the middle
            cities = [dest, maxCity]
            cities.sort()
            return str(maxDist+dist)+":"+cities[0]+":"+depart+":"+cities[1]
        return "NONE"




if __name__ == "__main__":
    path_calc = PathCalculator()
    sequence = ["CHI:NYC:719", "NYC:LA:2448", "NYC:HAWAII:4924"]
    for line in sequence:
        print(path_calc.process(line))



