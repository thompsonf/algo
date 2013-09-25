def count_inversions_and_sort(lst):
	if len(lst) <= 1:
		return lst, 0
	else:
		A = lst[:len(lst)/2]
		B = lst[len(lst)/2:]
		[C, invs_A] = count_inversions_and_sort(A)
		[D, invs_B] = count_inversions_and_sort(B)
		[E, split_invs] = merge_and_count_splitinv(C, D)
		return E, invs_A + invs_B + split_invs

def merge_and_count_splitinv(C, D):
	invs = 0
	lenC = len(C)
	lenD = len(D)
	idxC = 0
	idxD = 0
	E = []
	while lenC > 0 and lenD > 0:
		if C[idxC] <= D[idxD]:
			E.append(C[idxC])
			lenC -= 1
			idxC += 1
		elif C[idxC] > D[idxD]:
			E.append(D[idxD])
			lenD -= 1
			idxD += 1
			invs += lenC
	while lenC > 0:
		E.append(C[idxC])
		idxC += 1
		lenC -= 1
	while lenD > 0:
		E.append(D[idxD])
		idxD += 1
		lenD -= 1
	return E, invs