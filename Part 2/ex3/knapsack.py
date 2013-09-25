def knapsack(last_item_idx, size):
	if (last_item_idx, size) in prev_comps:
		return prev_comps[last_item_idx, size]
	else:
		if last_item_idx == -1:
			return 0
		else:
			ret = knapsack(last_item_idx - 1, size)
			if items[last_item_idx][1] <= size:
				ret = max(ret, knapsack(last_item_idx - 1, size - items[last_item_idx][1]) + items[last_item_idx][0])
			prev_comps[last_item_idx, size] = ret
			if len(prev_comps) % 10000 == 0:
				print(len(prev_comps))
			return ret

def load_knapsack_items(fname):
	f = open(fname)
	size, temp = [int(x) for x in f.readline().split()]
	knapsack_items = []
	for line in f:
		knapsack_items.append([int(x) for x in line.split()])
	return size, knapsack_items

#elements of knapsack_items should have value first weight second
size, items = load_knapsack_items("knapsack1.txt")
#elements of prev_comps are  (last_item_idx, size):optimal_val
prev_comps = {}

print(knapsack(len(items) - 1, size))