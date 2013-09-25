#maintain a set of all vertices
#maintain a dict of the leaders of each vertex
#maintain a dict of the "followers" of each vertex

#for each vertex
	#generate list of all neighbors
	#for each neighbor:
		#if neighbor exists and is not in same cluster
			#merge clusters

#yield all binary numbers of numbits bits which can be obtained by flipping 1 or 2 bits of vert
def yield_neighbors(vert, numbits):
	for i in range(numbits):
		yield vert ^ (1 << i)
	for i in range(numbits - 1):
		for j in range(i + 1, numbits):
			yield vert ^ ((1 << i) + (1 << j))

#return number of bits and set of all vertices (as integers)
def load_vert_set(fname):
	f = open(fname)
	numbits = int(f.readline().split()[1])
	vert_set = set()
	for bin_list in f:
		vert_set.add(int("".join(bin_list.split()), 2))
	return numbits, vert_set

def cluster(vert_set, numbits):
	followers = {i:{i} for i in vert_set}
	leader = {i:i for i in vert_set}

	num_processed = 0
	for v1 in vert_set:
		for v2 in yield_neighbors(v1, numbits):
			if v2 in vert_set:
				l1 = leader[v1]
				l2 = leader[v2]
				if l1 != l2:
					if len(followers[l1]) >= len(followers[l2]):
						for v in followers[l2]:
							leader[v] = l1
						followers[l1] |= followers[l2]
						del followers[l2]
					else:
						for v in followers[l1]:
							leader[v] = l2
						followers[l2] |= followers[l1]
						del followers[l1]
		num_processed += 1
		if num_processed % 1000 == 0:
			print(num_processed)

	return len(followers)

numbits, vert_set = load_vert_set("clustering_big.txt")
print(cluster(vert_set, numbits))