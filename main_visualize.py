#plotting functions for santa

	
def visualize(allEdges, allCities,pathnum):
	win = GraphWin("Visualize Path", 500,500)
	maxX = sorted(allCities, key = lambda x: x.getX())[-1]
	maxY = sorted(allCities, key = lambda x: x.getY())[-1]
	win = win.setCoords(0.0,0.0,maxX.getX(),maxY.getY())
	#draw all points
	for x in allCities:
		plotCity(win,x)
	path1, path2 = getPaths(allEdges)
	if pathnum==1:
		path = path1
	else:
		path = path2
	for y in path:
		plotEdge(win,edge)
	win.getMouse()
	
def plotEdge(win,edge):
	city1 = edge.getC1()
	city2 = edge.getC2()
	p1 = Point(city1.getX(), city1.getY())
	p2 = Point(city1.getX(), city1.getY())
	l = Line(p1,p2)
	l.draw(win)
	
def plotCity(win,city):
	p1 = Circle(Point(city.getX(), city.getY()),100)
	p1.draw(win)