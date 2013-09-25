def is2sum(i):
	for j in s:
		k = i - j
		if k != j and k in s:
			return True
	return False

s = set()
with open("algo1-programming_prob-2sum.txt") as f:
	for line in f:
		s.add(int(line.strip()))

count = 0
for i in range(-10000,10001):
	if i % 100 == 0:
		print(i)
		print("count = " + str(count))
	if is2sum(i):
		count += 1

print(count)