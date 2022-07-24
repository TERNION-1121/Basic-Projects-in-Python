def binary_search(arr, val):
    if val < arr[0] or val > arr[-1]: return -1
    else:
        end = len(arr) - 1
        start = 0
        mid = (end + start) // 2

        while end != start:
            if arr[mid] == val: return mid
            elif arr[mid] < val: start = mid + 1
            else: end = mid

            mid = (end + start) // 2
        
        return mid