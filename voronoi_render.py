import pyglet


class Voronoi_Render(object):

	def __init__(self,beachline):
		self.beachline = beachline

	def draw_beachline(self):
		drawn_sites = set()
		if self.beachline is None:
			print "self.beachline is None. Returning from draw_beachline without drawing."
			return

		#each is a tuple - (Site(Point),None) or (Breakpoint(Point),Breakpoint(Point))
		for t in self.beachline:
			#every site is a tuple of coordinates
			if len(t) is 2: #if two sets of coordinates are present, th
				pass
			else:
				pass


