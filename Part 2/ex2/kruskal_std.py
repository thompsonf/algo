from operator import itemgetter

#return number of vertices and list of edges with highest cost edge first
def load_edges(fname):
	f = open(fname)
	num_verts = int(f.readline().strip())
	g = [[int(x) for x in line.split()] for line in f]
	return num_verts, list(reversed(sorted(g, key=itemgetter(2))))

def clusters(num_verts, edges, fin_clusters):
	vert_set = {i:{i} for i in range(1, num_verts + 1)}
	leader = {i:i for i in range(1, num_verts + 1)}

	cur_clusters = num_verts
	while edges:
		v1, v2, temp = edges.pop()
		if cur_clusters <= fin_clusters:
			return temp
		l1 = leader[v1]
		l2 = leader[v2]
		if l1 != l2:
			if len(vert_set[l1]) >= len(vert_set[l2]):
				for v in vert_set[l2]:
					leader[v] = l1
				vert_set[l1] |= vert_set[l2]
				del vert_set[l2]
			else:
				for v in vert_set[l1]:
					leader[v] = l2
				vert_set[l2] |= vert_set[l1]
				del vert_set[l1]
			cur_clusters -= 1
			if cur_clusters == fin_clusters:
				break

	for v1, v2, dist in reversed(edges):
		if leader[v1] != leader[v2]:
			return dist


v, edges = load_edges("clustering1.txt")
print(clusters(v, edges, 4))