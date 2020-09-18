def findMaxSubArray(a):
	max_sum=max(a)
	list_max=[max(a)]
	for lists in [[a[j: j+i] for j in range(0,len(a)-i+1) if sum(a[j:j+i])>max_sum] for i in range(1,len(a)+1)]:
		for slice in lists:
			if max_sum<sum(slice):
				max_sum=sum(slice)
				list_max = slice
	return list_max
print(findMaxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
