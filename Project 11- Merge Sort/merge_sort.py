def mergeSort(arr: list):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    leftArray = arr[:mid]
    rightArray = arr[mid:]
    print(leftArray, rightArray)
    return merge(mergeSort(leftArray), mergeSort(rightArray))

def merge(leftArr: list, rightArr: list):
    resultArr = []
    rightIndex = 0
    leftIndex = 0

    while (leftIndex < len(leftArr) and rightIndex < len(rightArr)):
        if (leftArr[leftIndex] < rightArr[rightIndex]):
            resultArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            resultArr.append(rightArr[rightIndex])
            rightIndex += 1

    resultArr.extend(leftArr[leftIndex:])
    resultArr.extend(rightArr[rightIndex:])
    return resultArr