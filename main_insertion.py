#main insertion algorithm

from sys import maxint
from city import City
from main_func import importData, exportPaths
from main_dist import Dist

def selectStart(allCities, dist):
	'''I started with a start route is less than three cities
	the constraint is impossible to achieve'''
	start1 = [allCities[x] for x in [6,51,47,30,98]]
	start2 = [allCities[x] for x in [6,47,98,51,30]]
	for x in start1:
		x.visit()
	return [start1, start2]
	
def selectNext(dist, lastCity):
	#return dist.furthest(lastCity)
	return dist.closest(lastCity)

def allVisited(Cities):	#works
	"returns a boolean T/F conditional on whether all cities have been visited"
	for x in Cities:
		if x.status()==False:
			return False
	return True

def assignPath(paths, count):
	"Alternates which path is leading"
	if count % 2 == 0:
		return paths[0],paths[1]
	else:
		return paths[1],paths[0]

def insertCity(path, nextCity, dist, constraints = []):
	distPath = [dist.dist(nextCity,x) for x in path ]
	modifyDistPath(path, distPath, constraints)
	insertionIndex = getInsertionIndex(distPath)
	getConst = getAdj(insertionIndex,path)
	insertCityInPath(path,insertionIndex,nextCity)
	return getConst
	#return []
	
def getAdj(insertionIndex,path):
	toOut = []
	for h in [insertionIndex-1, insertionIndex]:
		if h >=0 and h<len(path):
			toOut.append(path[h])
	return toOut

def insertCityInPath(path,insertionIndex,nextCity):
	if insertionIndex < len(path):
		path.insert(insertionIndex, nextCity)
	else:
		path.append(nextCity)
	
def modifyDistPath(path, distPath, constraints):
	'''Modifies the path such that a zero is added to the front and back
	and so that any illegal routes are replaced with a large distance''' 
	if constraints != []:
		for adj in constraints:
			adjLocation = path.index(adj)
			distPath[adjLocation] = maxint / 2
	distPath.insert(0, 0)
	distPath.append(0)
	
def getInsertionIndex(distPath):
	'''Looks over modified distance path and picks the one that minimizes
	the sum of the two routes that would be added.  Insertion index is the
	SECOND of the two cities.  I.e. the new city should be inserted right
	before this index number'''
	count = 0
	minVal = maxint
	for i in range(len(distPath)-1):
		sumDist = distPath[i]+distPath[i+1]
		if sumDist < minVal:
			minVal = sumDist
			insertIndex = count
		count += 1
	return insertIndex

def furthestInsertion(allCities, dist):
	paths = selectStart(allCities,dist)
	lastCity = paths[0][-1]
	count = 0
	while not allVisited(allCities):
		nextCity = selectNext(dist, lastCity)
		leadPath, followPath = assignPath(paths, count)
		adjCity = insertCity(leadPath, nextCity, dist)
		insertCity(followPath, nextCity, dist, adjCity)
		nextCity.visit()
		lastCity = nextCity
		count += 1
		print count
	return paths