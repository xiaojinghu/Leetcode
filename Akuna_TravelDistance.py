from math import sin, cos, pi, acos
class solution(object):
    def calDistance(self,sequence, radius):
        # build a database to store the info
        database = {}
        res = []
        for item in sequence:
            # parse the input
            if item[0] == 'L':
                #it means that this is a location information, we store it in our 
                #database 
                inputType, city, latitude, longitude = item.split(':')
                database[city] = [float(latitude)*pi/180.0, float(longitude)*pi/180.0]
                res.append(city)
                continue
            else:
                inputType, passenger, depart, dest = item.split(':')
                latitudeDepart, longitudeDepart = database[depart]
                latitudeDest, longitudeDest = database[dest]
                deltaPhi = abs(longitudeDepart-longitudeDest)
                angle = acos(sin(latitudeDest)*sin(latitudeDepart)+cos(latitudeDest)*cos(latitudeDepart)*cos(deltaPhi))
                dis = int(radius*angle)
                print latitudeDepart, longitudeDepart, latitudeDest, longitudeDest, deltaPhi, angle, dis
                res.append(passenger+':'+depart+':'+dest+':'+str(dis))
        return res


obj = solution()
radius = 3958.8
sequence = ["LOC:CHI:41.836944:-87.684722", "LOC:NYC:40.7127:-74.0059", "TRIP:C0FFEE1C:CHI:NYC"]
print obj.calDistance(sequence, radius)

