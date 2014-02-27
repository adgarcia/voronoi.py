import pyglet
import voronoi_tesselation
import voronpi_render
import avl

def draw_arc(sweepline,site,breakpoint1,breakpoint2):
	vertex = Point(site.x,sweepline.y-site.y)

@window.event
def on_draw():
	window.clear()


if __name__ == '__main__':
	pyglet.app.run()

	'''
	*** I don't need to use an avl tree directly
	*** I just need a sortable list with instert,delete,find,sort times equivilent to an avl tree
	'''

	site_name = 'site'
	break_point_name = 'bp'

	window = pyglet.window.Window(800, 600,resizable=True)
	pyglet.gl.glClearColor(1, 1, 1, 1)
	point_res = 1 #1:1 point per pixel for arcs


'''
def compare(node1,node1):

	x1 = 0
	x2 = 0

	if node1 type is Site_Node
		pass
	else:
		pass

	if node2.type is BP_Node:
		pass
	else:
		pass

	return x1 < x2


class Site_Node(object):
	def __init__(self,site):
		self.site = site

class BP_Node(object):
	def __init__(self,site1,site2):
		self.left = site1
		self.right = site2
'''