#Code for DNA-inspired search algorithm

from main_func import unvisited
from random import randint
from city import City
from main_dist import distData

class Enzyme:
	def __init__(self, path, allCities):
		self.path = path
		self.allCities = allCities
		self.unvisited = allCities minus path #NEED TO LOOK UP ACTUAL SET NOTATION
		self.mistake = [] #keeps track of the one step that is not allowed if a mistake happens
		
		#initialize helicase and bind to a random city
		self.start = randint(len(allCities))
		Helicase = Helicase(path, self.start, allCities)
		Checker = Checker(path)
		
		mistakeLag = 40
		
		while self.unvisited != []:
			#bind to next that isn't in the mistake category
			Helicase.next(self.mistake)
			checkerLocation = Checker.getLocation()
			if len(path)>= checkerLocation + mistakeLag:
				#makes sure that helicase is atleast bind length away before moving checker
				if Checker.check():
					#if there's a mistake
					for i in range(mistakeLag-1):
						#pop out a length of the the mistakes minus 1
						temp = path.pop()
						temp.unvisit()
					#add the last one to be popped to mistake list
					mistake.append(path.pop())
					mistake[0].unvisit()
					Helicase.bind(checkerLocation)

class Helicase:
	def __init__(self,path, startCityNum, allCities):
		self.allCities = allCities
		self.city = startCityNum
		self.path = path
				
	def next(self, mistake):
		'''implements the greedy algorithm on the path'''
		self.unvisited = self.allCities minus self.path #set notation
		closest = self.best() #best needs to return two just in case one is the mistake
		if closest[0]==mistake[0]:
			#if the closest city is the old mistake, use the second one
			closest[0] = closest[1]
		path.append(closest) #adds best to the path
		mistake.pop() #cleans out the mistake que

	def best(self):
		self.city #minimum distance solution
		
			
	def bind(self,cityNum):
		'''moves the Helicase to a different part of the path'''
		self.city = cityNum
			
		
class Checker:
	def __init__(self, path):
		self.path = path
		self.binded = 0
	
	def check(self):
		self.n = len(path)
	
	def bind(self, num):
		self.binded = num
			
	def getLocation(self):
		return self.binded
	