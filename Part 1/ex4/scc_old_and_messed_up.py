from collections import Counter

# Note G[i] = [has_been_explored, number, leader, adjacencies...]

# n is number of vertices
def load_reversed_graph(fname, n):
	f = open(fname)
	graph = [None]*(n + 1)
	for line in f:
		ls = line.split()
		tail = int(ls[1])
		head = int(ls[0])
		if graph[tail] == None:
			graph[tail] = [False, 0, 0, head]
		else:
			graph[tail].append(head)
	for i in range(n):
		i += 1
		if graph[i] == None:
			graph[i] = [False, 0, 0]
	return graph

# n is number of vertices
def load_graph(fname, n):
	f = open(fname)
	graph = [None]*(n + 1)
	for line in f:
		ls = line.split()
		tail = int(ls[0])
		head = int(ls[1])
		if graph[tail] == None:
			graph[tail] = [False, 0, 0, head]
		else:
			graph[tail].append(head)
	for i in range(n):
		i += 1
		if graph[i] == None:
			graph[i] = [False, 0, 0]
	return graph

# n is number of vertices
def load_graph_with_replacements(fname, n, reps):
	f = open(fname)
	graph = [None]*(n + 1)
	for line in f:
		ls = line.split()
		tail = reps[int(ls[0])]
		head = reps[int(ls[1])]
		if graph[tail] == None:
			graph[tail] = [False, 0, 0, head]
		else:
			graph[tail].append(head)
	for i in range(n):
		i += 1
		if graph[i] == None:
			graph[i] = [False, 0, 0]
	return graph

def DFS(G, i):
	global t
	global s
	G[i][2] = s
	G[i][0] = True
	for j in G[i][3:]:
		if G[j][0] == False:
			DFS(G, j)
	t += 1
	G[i][1] = t

def DFS_stack(G, i):
	global t
	global s
	stack = [i]

	while len(stack) > 0:
		print(stack)
		j = stack[-1]
		if G[j][0] == False:
			G[j][2] = s
			G[j][0] = True
			stack += [x for x in G[j][3:] if (G[x][0] == False)]
		else:
			stack.pop()
			t += 1
			G[j][1] = t

def DFS_Loop(G, n):
	global t
	global s
	t = 0
	s = 0
	for i in reversed(range(n)):
		i += 1 # Adjust from 0-indexed to 1-indexed
		if G[i][0] == False:
			s = i
			DFS_stack(G, i)
			#DFS(G, i)

#fname = "SCC.txt"
#n = 875714
#fname = "small_scc.txt"
#n = 10
fname = "small_scc2.txt"
n = 12
s = 0
t = 0
Grev = load_reversed_graph(fname, n)
print("here")
DFS_Loop(Grev, n)
print("there")
reps = [lst[1] if lst != None else 0 for lst in Grev]
print(len(reps))
print(reps)
G = load_graph_with_replacements(fname, n, reps)
DFS_Loop(G, n)
leaders = [lst[2] if lst != None else 0 for lst in G]
c = Counter(leaders[1:])
scc_list = c.most_common(3)
print(scc_list)