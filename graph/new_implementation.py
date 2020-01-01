from enum import Enum
from collections import OrderedDict

class State(Enum):
	unvisited =1
	visited =2
	visiting =3

class Node:
	def __init__(self, num):
		self.num  = num
		self.state = State.unvisited
		self.adjecent =OrderedDict()

	def __str__(self):
		return self.num

class Graph:
	def __init__(self):
		self.nodes = OrderedDict()

	def add_node(self,num):
		self.nodes[num] = Node(num)

	def add_edge(self,sou, des, w=0):
		if sou not in self.nodes:
			self.add_node(sou)

		if des not in self.nodes:
			self.add_node(des)

		self.nodes[sou].adjecent[self.nodes[des]]=w

g= Graph()
g.add_edge(1,2,10)

print(g.nodes)