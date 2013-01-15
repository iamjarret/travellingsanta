#plotting functions for santa

from graphics import *

	
def visualize(paths, allCities):
	win = GraphWin("Visualize Path", 500,500)
	maxX = sorted(allCities, key = lambda x: x.getX())[-1]
	maxY = sorted(allCities, key = lambda x: x.getY())[-1]
	win = win.setCoords(0.0,0.0,maxX.getX(),maxY.getY())
	#draw all points
	path1, path2 = paths[0], paths[1]
	
	for x in range(len(path1)-1):
		cityLine(win, path1[x],path1[x+1])
	win.getMouse()
	
def plotEdge(win,edge):
	city1 = edge.getC1()
	city2 = edge.getC2()
	p1 = Point(city1.getX(), city1.getY())
	p2 = Point(city1.getX(), city1.getY())
	l = Line(p1,p2)
	l.draw(win)
	
def plotCity(win,city):
	p1 = Circle(pCity(city),100)
	p1.draw(win)
	
def pCity(city):
	return Point(city.getX(), city.getY())
	
def cityLine(win,c1,c2):
	l = Line(pCity(c1), pCity(c2))
	l.draw(win)