import time
start = time.time()

def partition(array, small, big):
    i = (small-1)         
    pivot = array[big]    
 
    for j in range(small, big):
 
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
 
    array[i+1], array[big] = array[big], array[i+1]
    return (i+1)

def quickSort(array, small, big):
    if len(array) == 1:
        return array
    if small < big:
        pi = partition(array, small, big)

        quickSort(array, small, pi-1)
        quickSort(array, pi+1, big)
 
array = [13, 9, 2, 17, 4, 7, 6, 11]
n = len(array)
quickSort(array, 0, n-1)
print("Sorted quickSort array:")
for i in range(n):
    print("%d" % array[i])


end = time.time()
print("running time: ")
print(end - start)

