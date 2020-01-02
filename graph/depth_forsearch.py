from collections import OrderedDict
g= OrderedDict({
	'a':set(['b','c']),
	'b':set(['a','d','e']),
	'c':set(['a','f']),
	'd':set(['b']),
	'e':set(['b','f']),
	'f':set(['c','e'])
})



def dfs(graph,start):
	visited =set()
	stack=[start]

	while stack:
		vertex =stack.pop()

		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex]-visited)
	return visited

print(dfs(g,'a'))


