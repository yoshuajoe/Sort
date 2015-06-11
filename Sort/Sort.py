from math import *

class DistanceComputation:
    def euclideanDist_p(self, mangoes, apples):
        temp = 0;
        for index in range(len(mangoes)):
            temp += pow(mangoes[index] - apples[index], 2)
        return sqrt(temp)
    
    def manhattanDist_p(self, mangoes, apples):
        temp = 0;
        for index in range(len(mangoes)):
            temp += abs(mangoes[index] - apples[index])
        return temp

    def manhattanDist_d(self, mangoes, apples): 
        temp = 0
        for key in mangoes:
            if key in apples:
                temp += abs(mangoes[key] - apples[key])
        return temp
    
    def euclideanDist_d(self, mangoes, apples): 
        temp = 0
        for key in mangoes:
            if key in apples:
                temp += pow((mangoes[key] - apples[key]), 2)
        return sqrt(temp) 
    
    def computeNearestNeighbor_dist(self, mangoes, apple, method):
        distances = []
        for mango in mangoes:
            if mango != apple:
                
                if method == 'manhattan' :
                    distance = manhattanDist_d(mangoes[mango], mangoes[apple])
                else:
                    distance = euclideanDist_d(mangoes[mango], mangoes[apple])
                
                distances.append(distance)
            return distances.sort()        

mangoes = [5,5]
apples = [4,2]
dist = DistanceComputation()
res = dist.manhattanDist(mangoes, apples)
print res