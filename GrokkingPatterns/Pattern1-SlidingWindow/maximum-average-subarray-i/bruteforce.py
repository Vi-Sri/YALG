

def bruteforce_maximum_average_subarray(arr: list, k: int):
    p = 0
    subarray_index = -1
    max_avg = -1
    index = 0
    while p+k < len(arr):
        sum = 0
        for j in range(k):
            sum += arr[p+j]
        avg = sum/k
        if avg > max_avg:
            max_avg = avg
            subarray_index = index 
        p += 1
        index += 1
    return max_avg, subarray_index
        

max_avg, subarray_index = bruteforce_maximum_average_subarray([1,12,-5,-6,50,3], 4)
print(f"Maximum sub array Average : {max_avg}, SubArray Index : {subarray_index}")