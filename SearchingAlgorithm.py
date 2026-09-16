# Linear search[(o(n))]
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i       # return index if found
    return -1              # return -1 if not found

# Example
arr = [10, 25, 3, 47, 8]
target = 47

result = linear_search(arr, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")

# Output: Found at index 3


# Binary search[(O(log n))]
def binary_search(nums, target):
    n = len(nums)

    l = 0
    r = n-1

    while l<=r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return -1