import math

def max(a,b):
	if a > b:
		return a
	return b

def min(a,b):
	if a < b:
		return a
	return b


#sorting varies between the data structures - each list should specify a lambda and call the sort function
'''
__cmp__(self, other)
Called by comparison operations if rich comparison (see above) is not defined.

Should return a negative integer if self < other
zero if self == other, a positive integer if self > other.
If no __cmp__(), __eq__() or __ne__() operation is defined, class instances are compared by object identity (``address'').
See also the description of __hash__() for some important notes on creating objects which support custom comparison operations
     and are usable as dictionary keys.
     (Note: the restriction that exceptions are not propagated by __cmp__() has been removed since Python 1.5.)
'''

#an arbitrary point in 2D space
class Point(object):

	def __init__(self,x=0,y=0):
		self.coordinates = (x,y)
		#self.x = x
		#self.y = y

	def distance(self,otherpoint):
		xcomp = (self.x-otherpoint.x)
		xcomp = xcomp * xcomp
		ycomp = (self.y-otherpoint.y)
		ycomp = ycomp * ycomp
		distanceSquared = xcomp+ycomp
		if distanceSquared == 0:
			return 0
		else:
			distance = math.sqrt(distanceSquared)
			return distance

	def max(self):
		if self.x > self.y:
			return self.x
		return self.y

	def __repr__(self):
		return repr(self.coordinates)

	def __eq__(self,other):
		return self.coordinates == other.coordinates

class Site(Point):
	#sites are used to define a site event
	def __init__(self,x=0,y=0):
		Point.__init__(self,x,y)
		self.breakpoints = None
		self.circle_event = None

class Breakpoint(Point):
	def __init__(self,x=0,y=0,left=None,right=None):
		self.left = left
		self.right = right
		Point.__init__(self,x,y)
		#add self to the bp list of left and right

	def __repr__(self):
		return repr((self.coordinates,self.left,self.right))

class Circle(Point):
	def __init__(self,x=0,y=0):
		Point.__init__(self,x,y)
		self.points = list()



'''
A container object
A list of these guys provides the finished voronoi diagram
'''
class Voronoi_Edge(object):
	def __init__(self,vertex1=None,vertex2=None,next=None,site=None,sibling=None):
		self.vertex1 = vertex1
		self.vertex2 = vertex2
		self.next_edge = next
		self.parent_site = site
		self.sibling = sibling

'''
created by circle events and when the algorithm terminates (to resolve the beachline)

class Voronoi_Vertex(Point):

	def __init__(self,edge):
		if edge.vertex1 is None:
			edge.vertex1 = self
		else if edge.vertex2 is None:
			edge.vertex2 = None
		else:
			#sanity check - this would be bad news
			print 'Well, shit. The Point at '
	def name(self):
		print "Voronoi_Vertex"
'''

class Voronoi_Site(Point):

	def __init__(self,x=0,y=0):
		self.circle_event = None
		self.beachline = None
		Point.__init__(self,x,y)

	def name(self):
		print "Voronoi_Site"

'''
**************************************EVENTS*************************************
When resolving events with the same priority, give precedence to circle events
*********************************************************************************
'''

class Event(object):
	def __init__(self,beachline=None,vertex_list=None):
		self.beachline = beachline
		self.vertex_list = vertex_list
class Site_Event(Event):
	def __init__(self,site,beachline,vertex_list):
		self.voronoi_site = site
		Event.__init__(self,beachline,vertex_list)





