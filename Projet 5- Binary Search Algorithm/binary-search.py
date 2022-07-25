def binary_search(arr, val):
        end = len(arr) - 1
        start = 0
        mid = (end + start) // 2

        while start <= end:
            if arr[mid] == val: return mid
            elif arr[mid] < val: start = mid + 1
            else: end = mid - 1
            mid = (end + start) // 2
            
        return -1