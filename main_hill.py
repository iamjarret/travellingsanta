#code for hill climbing

from city import City
from main_func import noSharedEdge
from sys import maxint
from random import shuffle
from main_dist import *

def randPaths(allCities):
	path1 = allCities[:]
	path2 = allCities[:]
	while not noSharedEdge([path1,path2]):
		shuffle(path1)
		shuffle(path2)
	return [path1, path2]
	
def reversedSections(paths):
	'''generator to return all possible variations 
	of two paths with parts switched'''
	for i,j in allPairs(len(paths[0])):
		if i != j:
			copiedPath=[]
			for i in range(2):
				copy=paths[i][:]
				if i < j:
					copy[i:j+1]=reversed(paths[i][i:j+1])
				else:
					copy[i+1:]=reversed(paths[i][:j])
					copy[:j]=reversed(paths[i][i+1:])
				if copy != paths[i]: # no point returning the same tour
					copiedPath.append(copy)
			yield copiedPath

def hillClimb(allCities, initFunc,moveOp,
	objFunc, maxBreadth):
	'''hillclimb alogirthm until we are at a local max or
	we've gone max_iter'''
	best = initFunc(allCities)
	bestScore = objFunc(best)
	numEval = 1
	track = [bestScore]
	while numEval <= maxBreadth:
		for next in moveOp(best):
			#if numEval >= maxBreadth:
			#	break
			nextScore = objFunc(next)
			numEval += 1
			if nextScore > bestScore:
				best, bestScore = next, nextScore
				track.append(bestScore)
				print bestScore
				numEval = 1
				break
	return best, track


def allPairs(size, shuffle = shuffle):
	r1=range(size)
	r2=range(size)
	if shuffle:
		shuffle(r1)
		shuffle(r2)
	for i in r1:
		for j in r2:
			yield (i,j)
			
def objFunc(paths):
	'''If there are no shared edges, return the longest path length
	if there are shared edges return the largest negative integer'''
	if noSharedEdge(paths):
		return -max(pathLength(paths[0]), pathLength(paths[1]))
	else:
		return -maxint