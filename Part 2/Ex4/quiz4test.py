#for a complete graph with num_verts vertices and all edge lengths -1, do
#the Floyd-Warshall algorithm as shown in class
num_verts = 10
A = {(i,j,k):0 for k in range(num_verts + 1) for j in range(1,num_verts + 1) for i in range(1,num_verts + 1)}
print(len(A))

for i in range(1,num_verts + 1):
	for j in range(1,num_verts + 1):
		if j != i:
			A[i,j,0] = -1

for k in range(1, num_verts + 1):
	for i in range(1, num_verts + 1):
		for j in range(1, num_verts + 1):
			 A[i,j,k] = min(A[i,j,k-1], A[i,k,k-1] + A[k,j,k-1])

for i in range(1,num_verts + 1):
	for j in range(1,num_verts + 1):
		print(A[i,j,num_verts])

print(len(A))
print(num_verts * num_verts * (num_verts + 1))