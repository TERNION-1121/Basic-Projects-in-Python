# Binary Search Algorithm
Given a sorted array of `n` elements, the algorithm searches for a given element `x` in the array and return the index of `x` in the array.
> For more information click on [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm).

<br>

**Binary Search** is a searching algorithm used in a _sorted_ array by repeatedly dividing the search interval in half.
The idea of binary search is to use the information that the array is **sorted**.

## Functioning

1. It begins with the mid element of the whole array as a search key.

-   ```py
    mid = (end + start) // 2
    ```

2. If the value of the search key is equal to the item, then it returns an index of the search key.

-   ```py 
    if arr[mid] == val: return mid
    ```

3. Or if the value of the search key is greater than the item in the middle of the interval, it narrows the interval to the upper half.  

-   ```py 
    elif arr[mid] < val: start = mid + 1
    ```
    
4. Otherwise, if the value of the search key is less than the item in the middle of the interval, it narrows it to the lower half.

-   ```py
    else: end = mid - 1
    ```
<hr>
    
The program repeatedly checks from the second point until the value is found or the interval is empty.

```py
 while start <= end:
            if arr[mid] == val: return mid
            elif arr[mid] < val: start = mid + 1
            else: end = mid - 1
            mid = (end + start) // 2
```

<br>
<br>

> If the value is not present in the array, the function returns `-1`, indicating the value was not found in the given array.
```py
return -1
```
