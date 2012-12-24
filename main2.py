from csv import reader
import math
from city import *
from edge import *
from main_func import importData
from main_alg import minEdgeAlg, assignEdge
from main_visualize import visualize #code not yet working

def importData(fileName):
	"Import lits of cities and creates City objects as list"
	csvfile = open(fileName)
	dataout = []
	for row in data:
		if row[0]!="id":
			row = row.strip().split(';')
			dataout.append(float(row[1]),float(row[2]))
	return dataout
	
def cartesianMatrix(coords):
	"Creates a distance matrix for city coords that uses straight line distance"
	matrix = {}
	for i, (x1,y1) in enumerate(coords):
		for j,(x2,y2) in enumerate(coords):
			dx,dy = x1-x2,y1-y2 
			dist = math.sqrt(dx*dx + dy*dy)
			matrix[i,j]=dist
	return matrix
	
def tourLength(matrix, tour):
	total = 0
	numCities = len(tour)
	for i in range(numCities):
		j = (i+1)%numCities
		city_i = tour[i]
		city_j = tour[j]
		total += matrix[city_i, city_j]
	return total
			
def main():
	#allCities = importData("santa_cities.csv")
	allCities = importData("santa_cities_test.csv")
	allEdges = minEdgeAlg(allCities)
	for x in allEdges[0:100]:
		print x.dist()
	assignEdge(allEdges)
	path1, path2 = getPaths(allEdges)
	visualize(allEdges, allCities, 1)
	
main()