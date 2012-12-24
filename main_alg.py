#The file contains the main sorting algorithms for santa project

from edge import *
from city import *
from graphics import *

def minEdgeAlg(allCities):
	for x in allCities:
		x.assignClosestCity(allCities)
	sortedCities = sorted(allCities, key = lambda x: x.getClosestDist())
	print len(sortedCities)
	allEdges = []	
	while not edgesComplete(allEdges, allCities):
	for y in sortedCities:
		newEdge = Edge(y, y.getClosestCity())
		if newEdge not in allEdges:
			allEdges.append(newEdge)
	return allEdges

def edgeComplete(allEdges, allCities):
	

def assignEdge(allEdges):
	count = 0
	for x in allEdges:
		c1 = x.getC1()
		c2 = x.getC2()
		if count%2==0:
			x.setPath(1)
			c1.visit(1)
			c2.visit(1)
		else:
			x.setPath(2)
			c1.visit(2)
			c2.visit(2)
		count +=1

def getPaths(allEdges):
	path1 = []
	path2 = []
	for x in allEdges:
		pathtemp = x.getPath()
		if pathtemp == 1:
			path1.append(x)
		elif pathtemp == 2:
			path2.append(x)
	return path1, path2