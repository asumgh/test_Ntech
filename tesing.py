def max_el(x):

	maxs = x[0]

	for i in x:
		if maxs<i:
			maxs = i

	return maxs


def summ(x):

	s = 0

	for i in x:
		s += i 

	return s


def findMaxSubArray(a):

	max_sum = max_el(a)
	list_max = [max_el(a)]

	for lists in [[a[j:j + i] for j in range(0, len(a) - i + 1) if summ(a[j:j + i])>max_sum] for i in range(1, len(a) + 1)]:
		for slice in lists:
			if max_sum<summ(slice):

				max_sum = summ(slice)
				list_max = slice

	return list_max
