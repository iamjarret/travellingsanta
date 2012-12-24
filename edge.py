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
		
	def __eq__(self, edge2):
		"defines == operator for Edge class"
		if self.c1 == edge2.getC1() and self.c2 == edge2.getC2():
			return True
		else:
			return False
		
	def __ne__(self,edge2):
		"defines != operate for Edge class"
		if self.c1 != edge2.getC1() or self.c2 != edge2.getC2():
			return True
		else:
			return False
			
	def setPath(self,num):
		self.path = num
		
	def getPath(self):
		return self.path
	
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