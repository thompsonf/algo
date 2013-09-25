min_range = -10000
max_range = 10000

def binary_search(x):
	# return the idx of the biggest number in lst that is <= x
	cur_min = 0
	cur_max = len(lst)
	while cur_min + 1 < cur_max:
		mid = (cur_min + cur_max) // 2
		midval = lst[mid]
		if midval < x:
			cur_min = mid + 1
		elif midval > x:
			cur_max = mid
		else:
			return mid
	return cur_min

s = set()
#with open("2-sum_test.txt") as f:
with open("algo1-programming_prob-2sum.txt") as f:
	for line in f:
		s.add(int(line.strip()))

lst = sorted(s)

sums = set()
for i in range(0, len(lst)):
	min_idx = max(i + 1, binary_search(min_range - lst[i]) - 1)
	max_idx = min(len(lst), binary_search(max_range - lst[i]) + 1)
	for j in range(min_idx, max_idx):
		t = lst[i] + lst[j]
		if t >= min_range and t <= max_range:
			sums.add(t)

#print(sums)
print(len(sums))