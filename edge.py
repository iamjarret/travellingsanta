#defines the Edge class

from city import *

class Edge:
	def __init__(self, city1, city2):
		"Initializes Edge class: saves c1 and c2 independent of original ordering"
		if city1.getX() > city2.getX():
			self.c1 = city1
			self.c2 = city2
		else:
			self.c1 = city2
			self.c2 = city1
		self.path = 0
	
	def __key(self):
		return (self.c1, self.c2)
		
	def __eq__(self,other):
		return self.__key() == other.__key()
	
	def __ne__(self,other):
		return self.key() != other.__key()
		
	def __hash__(self):
		return hash(self.__key())
	
	def dist(self):
		city1 = self.c1
		city2 = self.c2
		return city1.dist(city2)
			
	def getC1(self):
		"outputs c1 - one with larger x coordinate"
		return self.c1
		
	def getC2(self):
		"outputs c2 - one with smaller x coordinate"
		return self.c2