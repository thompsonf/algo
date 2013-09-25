from collections import Counter

# Note G[i] = [has_been_explored, number, leader, adjacencies...]
# Note G[i][0] is 0 if not explored, 1 if explored but not yet popped for the first time, 2 if already explored and popped
# G[i][1] is the label of node i
# G[i][2] is the leader of node i
# G[i][3:] is all of the edges leading from node i

# n is number of vertices
# load graph with reversed edges
def load_reversed_graph(fname, n):
	f = open(fname)
	graph = [None]*(n + 1)
	for line in f:
		ls = line.split()
		tail = int(ls[1])
		head = int(ls[0])
		if graph[tail] == None:
			graph[tail] = [0, 0, 0, head]
		else:
			graph[tail].append(head)
	for i in range(n):
		i += 1
		if graph[i] == None:
			graph[i] = [0, 0, 0]
	return graph

# n is number of vertices
# load graph with original edges
def load_graph(fname, n):
	f = open(fname)
	graph = [None]*(n + 1)
	for line in f:
		ls = line.split()
		tail = int(ls[0])
		head = int(ls[1])
		if graph[tail] == None:
			graph[tail] = [0, 0, 0, head]
		else:
			graph[tail].append(head)
	for i in range(n):
		i += 1
		if graph[i] == None:
			graph[i] = [0, 0, 0]
	return graph

# n is number of vertices
# load graph with edge i renamed to edge reps[i]
def load_graph_with_replacements(fname, n, reps):
	f = open(fname)
	graph = [None]*(n + 1)
	for line in f:
		ls = line.split()
		tail = reps[int(ls[0])]
		head = reps[int(ls[1])]
		if graph[tail] == None:
			graph[tail] = [0, 0, 0, head]
		else:
			graph[tail].append(head)
	for i in range(n):
		i += 1
		if graph[i] == None:
			graph[i] = [0, 0, 0]
	return graph

# perform depth first search with recursion
def DFS(G, i):
	global t
	global s
	G[i][2] = s
	G[i][0] = 1
	for j in G[i][3:]:
		if G[j][0] == 0:
			DFS(G, j)
	t += 1
	G[i][1] = t

# perform depth first search with stack
def DFS_stack(G, i):
	global t
	global s
	stack = [i]

	while len(stack) > 0:
		#print(stack)
		j = stack[-1]
		if G[j][0] == 0:
			G[j][2] = s
			G[j][0] = 1
			stack += [x for x in G[j][3:] if (G[x][0] == 0)]
		elif G[j][0] == 1:
			stack.pop()
			t += 1
			G[j][1] = t
			G[j][0] = 2
		else:
			stack.pop()

# s is the current "leader"
# t is the ordering. Lowest t means first completely explored
def DFS_Loop(G, n):
	global t
	global s
	t = 0
	s = 0
	for i in reversed(range(n)):
		i += 1 # Adjust from 0-indexed to 1-indexed
		if G[i][0] == 0:
			s = i
			DFS_stack(G, i)
			#DFS(G, i)

fname = "SCC.txt"
n = 875714
#fname = "small_scc.txt"
#n = 10
#fname = "small_scc2.txt"
#n = 12
s = 0
t = 0
Grev = load_reversed_graph(fname, n)
#print("here")
DFS_Loop(Grev, n)
#print("there")
reps = [lst[1] if lst != None else 0 for lst in Grev]
#print(len(reps))
#print(reps)
G = load_graph_with_replacements(fname, n, reps)
DFS_Loop(G, n)
leaders = [lst[2] if lst != None else 0 for lst in G]
c = Counter(leaders[1:])
scc_list = c.most_common(5)
print(scc_list)