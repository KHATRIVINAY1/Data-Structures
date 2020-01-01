class Vertex():
	"""docstring for Vertex"""
	def __init__(self, key):
		self.id = key
		self.connectedto={}


	def addNeighboor(self,nbr,weight =0):
		self.connectedto[nbr]=weight

	def getConnections(self):
		return self.connectedto.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedto[nbr]

	def __str__(self):
		return str(self.id)+ "connectedto"+ str([x.id for x in self.connectedto])


class Graph():
	"""docstring for Graph"""
	def __init__(self):
		self.vertlist ={}
		self.numVertices =0

	def addVertex(self,key):
		self.numVertices +=1
		newVertex = Vertex(key)
		self.vertlist[key] = newVertex
		return newVertex

	def getVertex(self,n):
		if n in self.vertlist:
			return self.vertlist[n]
		else:
			return None

	def addEdge(self,f,t,cost=0):
		if f not in self.vertlist:
			nv=self.addVertex(f)

		if t not in self.vertlist:
			nv =self.addVertex(t)

		self.vertlist[f].addNeighboor(self.vertlist[t],cost)

	def getVertices(self):
		return self.vertlist.keys()

	def __iter__(self):
		return iter(self.vertlist.values())

	def __contains__(self,n):
		return n in self.vertlist


g= Graph()
for i in range(6):
	g.addVertex(i)

print(g.vertlist.values())