comps = 0

def choose_pivot_pos(arr, st, end):
	#return st
	#return end
	mid = st + (end - st)/2
	if arr[st] < arr[end]:
		if arr[mid] < arr[st]:
			return st
		elif arr[mid] > arr[end]:
			return end
		else:
			return mid
	else:
		if arr[mid] < arr[end]:
			return end
		elif arr[mid] > arr[st]:
			return st
		else:
			return mid

def partition(arr, st, end):
	#choose a pivot
	piv_pos = choose_pivot_pos(arr, st, end)
	piv = arr[piv_pos]
	#swap the pivot with the first element
	temp_swap = arr[st]
	arr[st] = piv
	arr[piv_pos] = temp_swap
	#initialize indices
	i = st + 1
	for j in xrange(st + 1, end + 1):
		if arr[j] < piv:
			#swap arr[i] and arr[j]
			temp_swap = arr[j]
			arr[j] = arr[i]
			arr[i] = temp_swap
			i += 1
	#swap piv to its appropriate spot
	arr[st] = arr[i - 1]
	arr[i - 1] = piv
	return i - 2, i

def quicksort(arr, st, end):
	global comps
	comps += max(0, end - st)
	if st < end:
		#print st, " ", end
		#raw_input()
		left_end, right_st = partition(arr, st, end)
		quicksort(arr, st, left_end)
		quicksort(arr, right_st, end)

f = open("QuickSort.txt")
arr = [int(x.strip()) for x in f]
#arr = [3,2,1,4,6,4,8,7]
comps = 0
quicksort(arr, 0, len(arr) - 1)
print comps
print arr[:100]