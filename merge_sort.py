
'''
Merge Sort python
'''


def merge(left, right):
	results = []
	while left and right:
		if left[0] <= right[0]:
			results.append(left[0])
			left = left[1:]
		else:
			results.append(right[0])
			right = right[1:]
	while len(left) > 0:
		results.append(left[0])
		left = left[1:] 
	while len(right) > 0 :
		results.append(right[0])
		right = right[1:]
	return results


def merge_sort(input_list):
	if len(input_list)<=1:
		return input_list
	l = left = right = None
	middle = len(input_list)/2
	left = input_list[0:middle]
	right = input_list[middle : len(input_list)]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left, right)




x = merge_sort([11, 16, 12, 27, 23,1,2,3,4,2,3,5,7,9])
print x
