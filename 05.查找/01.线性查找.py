def linear_search(arr,x):
	n = len(arr)
	for i in range(n):
		if x == arr[i]:
			return 1
	return -1
	

if __name__ == "__main__":
	arr = [15,16,2,5,8,13,41]
	x = 8
	out = linear_search(arr,x)
	print(out)
	if out == 1:
		print(f"{x}在列表中")
	elif out == -1:
		print(f"{x}不在列表中")