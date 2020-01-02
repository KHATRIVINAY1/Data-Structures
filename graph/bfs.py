from collections import OrderedDict

g= OrderedDict({
	'a':set(['b','c']),
	'b':set(['a','d','e']),
	'c':set(['a','f']),
	'd':set(['b']),
	'e':set(['b','f']),
	'f':set(['c','e'])
})

def bfs(graph,start):
	visited =set()
	q = [start]
	while q:
		vertex = q.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			q.extend(graph[vertex]-visited)

	return visited

print(bfs(g,'a'))