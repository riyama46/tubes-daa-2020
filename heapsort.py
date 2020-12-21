import time

start = time.time() 
def heapify(array, j, k):
    max = k 
    left = 2 * k + 1    
    right = 2 * k + 2    
	
    if left < j and array[max] < array[left]:
        max = left
 
    if right < j and array[max] < array[right]:
        max = right
 
    if max != k:
        array[k], array[max] = array[max], array[k]
        heapify(array, j, max)
 
def heapSort(array):
    j = len(array)
 
    for k in range(j//2 - 1, -1, -1):
        heapify(array, j, k)
 
    for k in range(j-1, 0, -1):
        array[k], array[0] = array[0], array[k] 
        heapify(array, k, 0)
 

array = [3, 2, 8, 5, 3, 9, 13, 12]
heapSort(array)
j = len(array)
print("Sorted heapSort array:")
for k in range(j):
    print("%d" % array[k]),

end = time.time()
print("running time: ")
print(end - start)

