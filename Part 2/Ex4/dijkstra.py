from heapdict import heapdict

# note: heapq._siftdown(h, 0, i) takes a heap h that is correctly ordered except for
# h[i], and reorders the heap appropriately to get the invariant back

# NOTE: need to keep track of WHERE each vertex is in the heap. _siftdown
# doesn't seem to allow for that, so I will make my own heap implementation

# Need a "sift_up" for adding an element and a "sift_down" for removing an element.
# See wikipedia http://en.wikipedia.org/wiki/Binary_heap
# The heap will be stored in a list, and the sifts need to reorder the vector that
# tells which index in the heap each vertex is stored at in ADDITION to the heap itself

# for data from class:
# numverts = 200
# max_len = 1000000

def load_weighted_graph(fname, numverts):
	g = [[] for i in range(numverts)] # Note that this uses 0-based indexing! Vertex i will be at g[i - 1]
	with open(fname) as f:
		for line in f:
			ls = line.split();
			g[int(ls[0]) - 1] = [[int(x.split(',')[0]) - 1, int(x.split(',')[1])] for x in ls[1:]]
	return g

def dijkstra(g, start_vert):
	hd = heapdict()
	shortest_paths = {start_vert: 0} #len(g) is numverts

	add_new_verts_to_heap_dict(g, start_vert, hd, shortest_paths)

	while hd:
		(newmin_vert, score) = hd.popitem()
		shortest_paths[newmin_vert] = score
		add_new_verts_to_heap_dict(g, newmin_vert, hd, shortest_paths)

	return shortest_paths

# after adding v to the path
def add_new_verts_to_heap_dict(g, v, hd, shortest_paths):
	for u, weight in g[v]:
		if u not in shortest_paths:
			score = shortest_paths[v] + weight
			if u not in hd or score < hd[u]:
				hd[u] = score

g = load_weighted_graph("dijkstraData.txt", 200)
sp = dijkstra(g, 0)
ans = [sp[x-1] if x-1 in sp else 1000000 for x in [7,37,59,82,99,115,133,165,188,197]]
print(ans)