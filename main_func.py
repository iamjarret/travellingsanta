#santa.py

from csv import reader, writer
import math
from random import random
from city import *
from edge import *

def importData(fileName):
	"Import lits of cities and creates City objects as list"
	csvfile = open(fileName)
	dataout = []
	data = reader(csvfile, delimiter = ',')
	count = 0
	for row in data:
		if row[0]!="id":
			dataout.append(City(row[0],row[1],row[2]))
			count +=1
	return dataout
	
def exportPaths(paths, fileName):
	with open(fileName,'wb') as csvfile:
		writeFile = writer(csvfile)
		writeFile.writerow(["path1","path2","x1","y1","x2","y2"])
		for x in range(len(paths[0])):
			writeFile.writerow([paths[0][x].getId(),paths[1][x].getId(),paths[0][x].getX(),paths[0][x].getY(),paths[1][x].getX(),paths[1][x].getY()])
	
def importSolution(fileName):
	"Imports paths outputted as a solution"
	csvfile = open(fileName)
	path1 = []
	path2 = []
	data = reader(csvfile)
	count = 0
	for row in data:
		if row[0]!="path1":
			path1.append(int(row[0]))
			path2.append(int(row[1]))
			count +=1
	return path1, path2

	
def distance(City1, City2):
	"cartesian distance function between two cities: VERIFIED"
	return math.sqrt((City1.getX()-City2.getX())**2 + (City1.getY()-City2.getY())**2)

def unvisited(Cities): #works
	"Outputs the collection of cities that are unvisited by looping through the whole list."
	toout = []
	for x in Cities:
		if x.status()==False:
			toout.append(x)
	return toout

def allVisited(Cities):	#works
	"returns a boolean T/F conditional on whether all cities have been visited"
	for x in Cities:
		if x.status()==False:
			return False
	return True

def sortCities(Cities):
	return sorted(Cities, key = lambda Cities: Cities.pathnum)
	
def testpathLengthAll():
	"This function imports the test route and runs testpathLength - goal to verify scoring formulas: VERIFIED"
	AllCities = importData("santa_cities.csv")
	path1, path2 = importSolution("random_paths_benchmark.csv")
	testpathLength(path1, path2, AllCities)

def testpathLength(path1, path2, AllCities):
	"Given two paths and a data set, this function scores the routes."
	#need to implement a test that no edges are shared before finding the length
	count = 0
	for i in path1:
		AllCities[i].path(count)
		count += 1
	d1 = pathLength(AllCities)	
	count = 0
	for i in path2:
		AllCities[i].path(count)
		count += 1
	d2 = pathLength(AllCities)
	
	print "d1 is", d1
	print "d2 is", d2
	print "score is", max(d1,d2)
	return max(d1,d2)
	
def noSharedEdge(paths):
	'''takes a list of both paths and returns True if 
	there is no shared edge (i.e. the intersection of the sets
	is empty'''
	edge1, edge2 = pathToEdge(paths[0]), pathToEdge(paths[1])
	if set(edge1).intersection(set(edge2)) == set():
		return True
	else:
		return False
		
def pathToEdge(path):
	edges = []
	for i in range(len(path)-1):
		edges.append(Edge(path[i], path[i+1]))
	return edges