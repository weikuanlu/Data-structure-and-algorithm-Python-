def binary_search(arr,l,r,x):
	if l <= r:
		m = int((l+r)/2)
		if x == arr[m]:
			return m 
		elif x < arr[m]:
			return binary_search(arr,l,m-1,x)
		else:
			return binary_search(arr,m+1,r,x)

if __name__ == "__main__":
	arr = [15,25,35,46,48,59]
	index = binary_search(arr,0,len(arr)-1,46)
	print(index)