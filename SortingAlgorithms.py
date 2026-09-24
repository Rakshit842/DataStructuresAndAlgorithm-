# Bubble sort [(O(n^2))]
def bubbleSort(nums):
    n = len(nums)

    for i in range(n):
        isSwap = False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isSwap = True

            if not isSwap:
                break

    return nums 


# selection sort[(O(n^2))]
def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        mn = nums[i]
        ind = i
        for j in range(i+1, n):
            if nums[j]<mn:
                mn = nums[j]
                ind = j

        temp = nums[i]
        nums[i] = nums[ind]
        nums[ind] = temp
    return nums 

            

# insertion sort[(O(n^2))]
def insertionSort(nums):
    n = len(nums)

    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1] = key

    return nums


# Merge sort[O(n log(n))]
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left  = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]);  i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]


# Quick sort[(O(n^2))]
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]   # last element as pivot
    i = low - 1         # index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test
print(quick_sort([10, 7, 8, 9, 1, 5]))
# Output: [1, 5, 7, 8, 9, 10]


# Counting sort[(O(mx))]
def counting_sort(nums):
    n = len(nums)
    mx = max(nums)

    freq = [0]*(mx+1)

    for i in nums:
        freq[i]+=1

    nums=[]

    for i in range(0, mx+1):
        while freq[i]>0:
            nums.append(i)
            freq[i]-=1

    return nums    

# two pointer sorting
def two_points(nums):
    left = 0
    right = len(nums) - 1
    i = 0

    while i <= right:
        if nums[i] == 1:
            i+=1
        elif nums[i] == 0:
            temp = nums[i]
            nums[i] = nums[left]
            nums[left] = temp 
            i += 1
            left += 1

        else:
            temp = nums[i]
            nums[i] = nums[right]
            nums[right] = temp 
            right -= 1

