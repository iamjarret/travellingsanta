#Creates distance framework

from sys import maxint
from math import sqrt
from city import City

def distance(City1, City2):
	"cartesian distance function between two cities: VERIFIED"
	return sqrt((City1.getX()-City2.getX())**2 + (City1.getY()-City2.getY())**2)
	
def pathLength(Cities, dist):
	distAmt = 0
	for i in range(len(Cities)-1):
		distAmt += dist.dist(Cities[i],Cities[i+1])
	return distAmt

def evaluate(paths, dist):
	return max(pathLength(paths[0],dist), pathLength(paths[1],dist))
	
class Dist:
	def __init__(self, allCities):
		self.allCities = allCities
		#self.distMatrix = [ [distance(c1,c2) for c1 in allCities] for c2 in allCities ]
		self.unvisitedList = self.unvisited()
		
	def unvisited(self):
		"Outputs the collection of cities that are unvisited by looping through the whole list."
		toout = []
		for x in self.allCities:
			if x.status()==False:
				toout.append(x.getId())
		return toout
	
	def unvisitedCities(self):
		"Outputs the collection of cities that are unvisited by looping through the whole list."
		toout = []	
		for x in self.allCities:
			if x.status()==False:
				toout.append(x)
		return toout
		
	def closest(self, c1):
		'''Returns closest unvisited city to c1'''
		self.unvisitedCityList = self.unvisitedCities()
		count = 0
		minVal = maxint
		#for value in self.distMatrix[cId]:
		for x in self.unvisitedCityList:			
			distTemp = distance(x,c1)
			if distTemp < minVal and distTemp > 0:
				minVal = distTemp
				minCity = x
			count +=1
		return minCity
	
	def furthest(self,c1):
		'''Returns furthese unvisited city to c1'''
		self.unvisitedCityList = self.unvisitedCities()
		count = 0
		maxVal = 0
		for x in self.unvisitedCityList:
			value = distance(x,c1)
			if value > maxVal:
				maxVal = value
				maxCity = x
			count +=1
		return maxCity
	
	def dist(self,c1,c2):
		#cId1 = c1.getId()
		#cId2 = c2.getId()
		#return self.distMatrix[cId1][cId2]
		return distance(c1,c2)
	
	def getMatrix(self):
		return self.distMatrix	
		
	def density(self, c1):
		'''Adds up distance of 10 closest cities.  Lower the number the region around the city'''
		cId = c1.getId()
		sortedDist = sorted(self.distMatrix[cId])
		return sum(sortedDist[0:self.densityValue-1])