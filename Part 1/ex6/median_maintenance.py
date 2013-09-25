from heapq import *

to_be_processed = []
with open("Median.txt") as f:
	for line in f:
		to_be_processed.append(int(line.strip()))

to_be_processed.reverse()
lowheap = []
highheap = []
sum = 0
while to_be_processed:
	cur = to_be_processed.pop()
	if len(highheap) == 0 or cur < highheap[0]:
		heappush(lowheap, -cur)
	else:
		heappush(highheap, cur)
	if len(lowheap) < len(highheap):
		heappush(lowheap, -heappop(highheap))
	elif len(lowheap) > len(highheap) + 1:
		heappush(highheap, -heappop(lowheap))
	sum += -lowheap[0]

print(sum % 10000)