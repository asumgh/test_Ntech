def findMaxSubArray(a):
	"""Finding a continuous subarray in the array containing at least one number that has the largest sum. Input: list; Output: list"""
	max_sum = max(a)
	list_max = [max(a)]

	for lists in [[a[j:j + i] for j in range(0, len(a) - i + 1) if sum(a[j:j + i])>max_sum] for i in range(1, len(a) + 1)]:
		for slice in lists:
			if max_sum<sum(slice):

				max_sum = sum(slice)
				list_max = slice

	return list_max
