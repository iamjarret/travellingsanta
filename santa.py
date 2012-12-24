#santa.py

def importData(fileName):
	"Import lits of cities and creates City objects as list"
	csvfile = open(fileName)
	dataout = []
	data = reader(csvfile)
	count = 0
	for row in data:
		if row[0]!="id":
			dataout.append(City(row[1],row[2]))
			count +=1
	return dataout
	
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
	
def pathLength(Cities):
	"Sorts cities based on pathNum then calculates distance: VERIFIED"
	dist = 0
	sortedCities = sortCities(Cities)
	for i in range(len(sortedCities)-1):
		dist += distance(sortedCities[i],sortedCities[i+1])
	return dist

def sortCities(Cities):
	return sorted(Cities, key = lambda Cities: Cities.pathnum)
	
def testpathLengthAll():
	"This function imports the test route and runs testpathLength - goal to verify scoring formulas: VERIFIED"
	AllCities = importData("santa_cities.csv")
	path1, path2 = importSolution("random_paths_benchmark.csv")
	testpathLength(path1, path2, AllCities)

def testpathLength(path1, path2, AllCities=importData("santa_cities.csv")):
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
	
def randomPath(dataAll = importData("santa_cities.csv")):
	"Randomly selects Cities from dataAll.  Outputs City number."
	tosort=[]
	for i in range(len(dataAll)):
		tosort.append([random(),i])
	sort = sorted(tosort)
	outlist = []
	for x in sort:
		outlist.append(x[1])
	return outlist	
	
def main():
	#right now the main code implements the randomPath() function to
	#find two paths.

	min = 9999999999999
	for i in range(100):
		r1 = randomPath()
		r2 = randomPath()
		pathlen = testpathLength(r1,r2)
		if pathlen<min:
			min = pathlen
			path1 = r1
			path2 = r2
		print min
	savePaths(path1,path2,filename) #need to implement		
