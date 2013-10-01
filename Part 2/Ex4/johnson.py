from heapdict import heapdict
from copy import deepcopy

def load_graph(fname):
	f = open(fname)
	f.readline()
	g = {}
	g_rev = {}
	verts = set()
	for line in f:
		tail, head, weight = [int(x) for x in line.split()]
		verts.add(tail)
		verts.add(head)
		if tail in g:
			g[tail].append((head, weight))
		else:
			g[tail] = [(head, weight)]
		if head in g_rev:
			g_rev[head].append((tail, weight))
		else:
			g_rev[head] = [(tail, weight)]
	return g, g_rev, verts

def add_zero_vert(g, g_rev, verts, s):
	h = deepcopy(g)
	h_rev = deepcopy(g_rev)
	h_verts = deepcopy(verts)
	if s not in g:
		h[s] = [(v, 0) for v in h_verts]
		for v in verts:
			if v in h_rev:
				h_rev[v].append((s,0))
			else:
				h_rev[v] = [(s,0)]
		h_verts.add(s)
		return h, h_rev, h_verts
	else:
		print("Something is wrong!")
		return False

def bellman_ford(g, g_rev, verts, s):
	inf = float("inf")
	#add new vertex labeled -1 that has 0-weight edges to all others
	n = len(verts)
	#setup the 2D array
	#+1 is for the new vert
	A = {(i, v):inf for i in range(n) for v in verts}
	A[0,s] = 0

	for i in range(1, n + 1):
		for v in verts:
			#calculate min(w,v) in E of {A[i - 1, w] + c_wv}
			cur_min_weight = A[i - 1, v]
			if v in g_rev:
				for w, c in g_rev[v]:
					new_weight = A[i - 1, w] + c
					if new_weight < cur_min_weight:
						cur_min_weight = new_weight
			A[i, v] = cur_min_weight
	#check for a negative-cost cycle
	for v in verts:
		if A[n - 1, v] != A[n, v]:
			return False
	return {v:A[n - 1, v] for v in verts}

def reweight(g, g_rev, verts):
	s = -1
	h, h_rev, h_verts = add_zero_vert(g, g_rev, verts, s)
	print("before bf")
	p_dict = bellman_ford(h, h_rev, h_verts, s)
	print("after bf")
	if p_dict == False:
		return False, False, False

	g_rw = {}
	g_rev_rw = {}

	for u in verts:
		if u in g:
			g_rw[u] = [(v, c + p_dict[u] - p_dict[v]) for (v, c) in g[u]]
	for v in verts:
		if v in g_rev:
			g_rev_rw[v] = [(u, c + p_dict[u] - p_dict[v]) for (u, c) in g_rev[v]]
	return g_rw, g_rev_rw, p_dict

#DIJKSTRA ISN'T WORKING. PROBABLY DUE TO THE FACT THAT NOT EVERYTHING CAN BE REACHED FROM
#THE SOURCE VERTEX
def dijkstra(g, start_vert):
	hd = heapdict()
	shortest_paths = {start_vert: 0}

	add_new_verts_to_heap_dict(g, start_vert, hd, shortest_paths)

	while hd:
		(newmin_vert, score) = hd.popitem()
		shortest_paths[newmin_vert] = score
		add_new_verts_to_heap_dict(g, newmin_vert, hd, shortest_paths)

	return shortest_paths

def add_new_verts_to_heap_dict(g, v, hd, shortest_paths):
	if v in g:
		for u, weight in g[v]:
			if u not in shortest_paths:
				score = shortest_paths[v] + weight
				if u not in hd or score < hd[u]:
					hd[u] = score

def johnson(g, g_rev, verts):
	h, h_rev, p_dict = reweight(g, g_rev, verts)
	if h == False:
		return False
	cur_min_weight = float("inf")
	num_done = 0
	L = len(verts)
	for v in verts:
		print("num done: %d of %d" % (num_done, L))
		sp = dijkstra(h, v)
		for w in sp:
			cur_weight = sp[w] - p_dict[v] + p_dict[w]
			if cur_weight < cur_min_weight:
				cur_min_weight = cur_weight
		num_done += 1
	return cur_min_weight



g, gr, v = load_graph("g3.txt")
w = johnson(g, gr, v)
print(w)