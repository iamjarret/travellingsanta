#defines the City class

import math

class City:
	def __init__(self, x,y):
		"Creates City object for storing City data"
		self.x = int(x)
		self.y = int(y)
		self.pathnum = 0
		self.visited1 = False
		self.visited2 = False
		self.visited = False
		self.dead = False
		self.dead1 = False
		self.dead2 = False
	
	def visit(self,path):
		"self.visit() makes the City have status visitied"
		if path==1:
			if self.visited1:
				self.dead1=True
			else:
				self.visited1 = True
		elif path==2:
			if self.visited2:
				self.dead2 = True
			else:
				self.visited2 = True
		else:
			if self.visited:
				self.dead = True
			else:
				self.visited = True
				
	def reset(self):
		"resets the City status to unvisited"
		self.visited = False
		
	def getX(self):
		"Prints x coordinate of City"
		return self.x
		
	def getY(self):
		"Prints y coordinated of City"
		return self.y
	
	def getX1(self):
		"Prints x1 coordinate of City"
		return self.x1
		
	def getY1(self):
		"Prints y1 coordinated of City"
		return self.y1
	
	def getX2(self):
		"Prints x2 coordinate of City"
		return self.x2
		
	def getY2(self):
		"Prints y2 coordinated of City"
		return self.y2
	
	def move1(self,dx,dy):
		self.x1 += dx
		self.y1 += dy
	
	def move2(self,dx,dy):
		self.x2 += dx
		self.y2 += dy
		
	def path(self,number):
		"City stores what number it is in the path as pathnum"
		self.pathnum = number
		
	def getPath(self):
		"Prints pathnum"
		return self.pathnum
		
	def status(self, path):
		"returns City visit/unvisited status for each path"
		if path ==1:
			return self.visited1
		else:
			return self.visited2
			
	def dist(self, City2):
		"returns absolute euclidian distance"
		return math.sqrt((self.x-City2.getX())**2 + (self.y-City2.getY())**2)

	def dist1(self, City2):
		"returns distance for path 1 Euclidian"
		return math.sqrt((self.x1-City2.getX1())**2 + (self.y1-City2.getY1())**2)
		
	def dist2(self, City2):
		"returns distance for path 2 Euclidian"
		return math.sqrt((self.x2-City2.getX2())**2 + (self.y2-City2.getY2())**2)
		
	def assignClosestCity(self, allCities):
		"gets closest city to self from a list of cities"
		self.closest = sorted(allCities, key = lambda city: self.dist(city))[1]
		self.closestDist = self.dist(self.closest)
		
	def reassignClosestCity(self, allCities, allEdges):
		
	
	def getClosestDist(self):
		return self.closestDist
		
	def getClosestCity(self):
		return self.closest
		