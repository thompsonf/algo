def load_graph(fname):
	f = open(fname)
	f.readline()
	g = {}
	verts = set()
	for line in f:
		start, end, weight = [int(x) for x in line.split()]
		verts.add(start)
		verts.add(end)
		if start in g:
			g[start].append([end, weight])
		else:
			g[start] = [[end, weight]]
		if end in g:
			g[end].append([start, weight])
		else:
			g[end] = [[start, weight]]
	return g, verts

def naive_prim(g, verts):
	#assuming that 1 will always be a vertex
	T = {1}
	X = verts - T
	total_cost = 0
	while X:
		if len(X) % 10 == 0:
			print(len(X))
		cur_min_weight = None
		cur_min_edge = [None, None]
		for v in T:
			for edge in g[v]:
				if edge[0] in X and (cur_min_weight == None or cur_min_weight > edge[1]):
					cur_min_weight = edge[1]
					cur_min_edge = [v, edge[0]]
		T.add(cur_min_edge[1])
		X.remove(cur_min_edge[1])
		total_cost += cur_min_weight
	return total_cost
