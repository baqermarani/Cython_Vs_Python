
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1 , len(arr) ):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def selection_sort_optimized(list arr):
    cdef int i , j , min_index
    cdef int temp
    cdef int n = len(arr)
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1 , len(arr)-1):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    list = [x for x in arr[:n+1]]
    return list