from csv import reader
import math
from city import City
from edge import Edge
from main_func import importData, exportPaths, noSharedEdge
from main_hill import *
from main_dist import Dist, evaluate
from main_insertion import furthestInsertion

def main():
	allCities = importData("santa_cities.csv")
	#allCities = importData("santa_cities_test.csv")
	dist = Dist(allCities)
	print "done with dist matrix"
	bestPath = furthestInsertion(allCities, dist)
	print evaluate(bestPath, dist)
	exportPaths(bestPath, "run1.csv")
	print noSharedEdge(bestPath)
	#visualize(bestPath, allCities)
	
main()