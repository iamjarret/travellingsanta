from csv import reader
import math
from city import *
from edge import *
from main_func import importData
from main_alg import minEdgeAlg, assignEdge
from main_visualize import visualize #code not yet working


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