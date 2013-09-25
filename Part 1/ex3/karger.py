import random
import copy

def loadGraph(fname):
	f = open(fname)
	ret = {}
	for line in f:
		splitline = line.split()
		splitline = [int(x) for x in splitline]
		ret[splitline[0]] = splitline[1:]
	return ret

def contract(graph, v1, v2):
	graph[v1] = [x for x in graph[v1] if x != v2] + [x for x in graph[v2] if x!= v1]
	del graph[v2]
	for key in graph:
		for n, v in enumerate(graph[key]):
			if v == v2:
				graph[key][n] = v1

def findRandomEdge(graph):
	return random.choice([(k,v) for k in graph for v in graph[k]])

def karger(graph):
	while len(graph) > 2:
		k, v = findRandomEdge(graph)
		contract(graph, k, v)
	k, v = graph.popitem()
	return len(v)

def repeatedKarger(graph, num):
	cur_min = -1;
	for i in range(num):
		g = copy.deepcopy(graph)
		ret = karger(g)
		print(ret)
		if cur_min == -1 or ret < cur_min:
			cur_min = ret
	return cur_min