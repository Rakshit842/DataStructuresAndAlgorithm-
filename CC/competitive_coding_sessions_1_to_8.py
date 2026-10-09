"""
COMPETITIVE CODING SYLLABUS — SESSIONS 1–8
Python reference implementations with time/space complexity.

Conventions:
- Functions are written for learning and LeetCode-style use.
- "Remove duplicates" assumes a sorted array and returns the new logical length;
  the unique values occupy nums[:length].
- "Pivot index" means an index where left sum equals right sum.
- "Count elements with maximum frequency" returns the sum of frequencies of
  all values tied for the maximum frequency (LeetCode 3005 interpretation).
- "Aggressive cows" assumes positions can be sorted and cows >= 2.
"""

from collections import Counter
from typing import List


# ============================================================
# SESSION 1 — PROBLEM-SOLVING APPROACH (no specific algorithm)
# ============================================================
# 1. Understand input/output and constraints.
# 2. Try a small example by hand.
# 3. Start with a brute-force approach.
# 4. Identify repeated work / sorted properties / useful data structures.
# 5. Improve complexity, prove correctness, test edge cases.
# 6. State time and auxiliary-space complexity.


# ============================================================
# SESSION 2 — RECURSION
# ============================================================

def factorial(n: int) -> int:
    """n!; assumes n >= 0. Time O(n), recursion stack O(n)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def power(x: int, n: int) -> int:
    """x^n for n >= 0 using exponentiation by squaring.
    Time O(log n), recursion stack O(log n).
    """
    if n < 0:
        raise ValueError("This version expects n >= 0")
    if n == 0:
        return 1
    half = power(x, n // 2)
    result = half * half
    return result if n % 2 == 0 else result * x


def print_increasing(n: int) -> None:
    """Print 1..n. Time O(n), stack O(n)."""
    if n <= 0:
        return
    print_increasing(n - 1)
    print(n)


def print_decreasing(n: int) -> None:
    """Print n..1. Time O(n), stack O(n)."""
    if n <= 0:
        return
    print(n)
    print_decreasing(n - 1)


def print_decreasing_then_increasing(n: int) -> None:
    """Print n..1..n. Time O(n), stack O(n)."""
    if n <= 0:
        return
    print(n)
    print_decreasing_then_increasing(n - 1)
    print(n)


def print_increasing_then_decreasing(n: int) -> None:
    """Print 1..n..1. Time O(n), stack O(n)."""
    if n <= 0:
        return
    print_increasing_then_decreasing(n - 1)
    print(n)
    print_increasing_then_decreasing(n - 1)


def count_digits(n: int) -> int:
    """Number of digits; 0 has one digit. Time O(log10 |n|), stack O(1)."""
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def recursive_array_sum(nums: List[int], index: int = 0) -> int:
    """Sum nums[index:]. Time O(n), recursion stack O(n)."""
    if index == len(nums):
        return 0
    return nums[index] + recursive_array_sum(nums, index + 1)


# ============================================================
# SESSION 3 — RECURSION II
# ============================================================

def pivot_index(nums: List[int]) -> int:
    """First index where left sum == right sum. Time O(n), space O(1)."""
    total = sum(nums)
    left_sum = 0
    for i, value in enumerate(nums):
        if left_sum == total - left_sum - value:
            return i
        left_sum += value
    return -1


def remove_duplicates_sorted(nums: List[int]) -> int:
    """In-place unique compaction for sorted nums.
    Returns k; unique values are nums[:k]. Time O(n), extra space O(1).
    """
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def fibonacci(n: int) -> int:
    """F(0)=0, F(1)=1. Iterative optimal standard solution:
    Time O(n), extra space O(1).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def tower_of_hanoi(n: int, source: str = "A",
                   auxiliary: str = "B", target: str = "C") -> None:
    """Print optimal moves. Time/output O(2^n), stack O(n)."""
    if n <= 0:
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


# Recursion-tree note:
# T(n) = 2T(n-1) + O(1) for naive recursive Fibonacci/Hanoi-style branching
# gives exponential work in the naive Fibonacci version. Memoization reduces
# Fibonacci to O(n) time and O(n) space; iterative Fibonacci uses O(1) space.


# ============================================================
# SESSION 4 — ARRAY I
# ============================================================

def max_subarray_sum(nums: List[int]) -> int:
    """Kadane's algorithm; non-empty input. Time O(n), space O(1)."""
    if not nums:
        raise ValueError("nums must be non-empty")
    current = best = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best


def max_product_subarray(nums: List[int]) -> int:
    """Track maximum and minimum products (negative can flip sign).
    Time O(n), space O(1). Assumes non-empty input.
    """
    if not nums:
        raise ValueError("nums must be non-empty")
    max_here = min_here = answer = nums[0]
    for x in nums[1:]:
        if x < 0:
            max_here, min_here = min_here, max_here
        max_here = max(x, max_here * x)
        min_here = min(x, min_here * x)
        answer = max(answer, max_here)
    return answer


def majority_element(nums: List[int]) -> int:
    """Moore's voting algorithm. O(n) time, O(1) space.
    Assumes a majority element (> n//2 occurrences) exists.
    """
    candidate = None
    votes = 0
    for x in nums:
        if votes == 0:
            candidate = x
        votes += 1 if x == candidate else -1
    return candidate


# ============================================================
# SESSION 5 — ARRAY II
# ============================================================

def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of a pair. Expected O(n) time, O(n) space."""
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


def sum_of_max_frequency_elements(nums: List[int]) -> int:
    """Sum frequencies of all values tied at the maximum frequency.
    Time O(n), space O(n).
    """
    if not nums:
        return 0
    counts = Counter(nums)
    highest = max(counts.values())
    return sum(freq for freq in counts.values() if freq == highest)


def rotate_right(nums: List[int], k: int) -> None:
    """Rotate list in-place right by k. Time O(n), extra space O(1)."""
    n = len(nums)
    if n == 0:
        return
    k %= n

    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


def rotate_left(nums: List[int], k: int) -> None:
    """Rotate list in-place left by k. Time O(n), extra space O(1)."""
    n = len(nums)
    if n == 0:
        return
    k %= n

    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)


# ============================================================
# SESSION 6 — ARRAY III / TWO POINTERS
# ============================================================

def sort_colors(nums: List[int]) -> None:
    """Sort values 0, 1, 2 in-place (Dutch National Flag).
    Time O(n), space O(1).
    """
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


def max_area(height: List[int]) -> int:
    """Container With Most Water. Time O(n), space O(1)."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


def trap_rain_water(height: List[int]) -> int:
    """Two-pointer trapping rain water. Time O(n), space O(1)."""
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


# ============================================================
# SESSION 7 — BINARY SEARCH I
# ============================================================

def lower_bound(nums: List[int], target: int) -> int:
    """First index i where nums[i] >= target; returns len(nums) if absent.
    Requires sorted nums. Time O(log n), space O(1).
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(nums: List[int], target: int) -> int:
    """First index i where nums[i] > target; returns len(nums) if absent.
    Requires sorted nums. Time O(log n), space O(1).
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def min_eating_speed(piles: List[int], h: int) -> int:
    """Koko Eating Bananas. Time O(n log(max(piles))), space O(1)."""
    left, right = 1, max(piles)

    def can_finish(speed: int) -> bool:
        hours = sum((pile + speed - 1) // speed for pile in piles)
        return hours <= h

    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    return left


# LeetCode-style First Bad Version template:
# The platform supplies isBadVersion(version). Do not define it locally
# when submitting on LeetCode.
def first_bad_version(n: int, is_bad_version) -> int:
    """Find first bad version. Time O(log n), space O(1)."""
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left


# ============================================================
# SESSION 8 — BINARY SEARCH II
# ============================================================

def search_rotated(nums: List[int], target: int) -> int:
    """Distinct values; rotated sorted array. Time O(log n), space O(1)."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def search_rotated_with_duplicates(nums: List[int], target: int) -> bool:
    """Duplicate values allowed. Average O(log n), worst O(n), space O(1)."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True

        # Duplicates hide which half is sorted; safely shrink boundaries.
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


def aggressive_cows(stalls: List[int], cows: int) -> int:
    """Maximum possible minimum distance between any two placed cows.
    Time O(n log(range)), space O(1) extra apart from sorting.
    """
    if cows <= 1:
        return 0
    stalls.sort()
    if cows > len(stalls):
        raise ValueError("Number of cows cannot exceed number of stalls")

    def can_place(distance: int) -> bool:
        placed = 1
        last = stalls[0]
        for position in stalls[1:]:
            if position - last >= distance:
                placed += 1
                last = position
                if placed >= cows:
                    return True
        return False

    left, right = 1, stalls[-1] - stalls[0]
    answer = 0
    while left <= right:
        mid = left + (right - left) // 2
        if can_place(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


# ============================================================
# QUICK SELF-TESTS — run this file directly to check examples
# ============================================================
if __name__ == "__main__":
    assert factorial(5) == 120
    assert power(2, 10) == 1024
    assert count_digits(0) == 1
    assert count_digits(-1234) == 4
    assert recursive_array_sum([1, 2, 3, 4]) == 10
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    sample = [1, 1, 2, 2, 3]
    k = remove_duplicates_sorted(sample)
    assert sample[:k] == [1, 2, 3]
    assert fibonacci(10) == 55
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_product_subarray([2, 3, -2, 4]) == 6
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert sum_of_max_frequency_elements([1, 2, 2, 3, 1, 4]) == 4
    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate_right(arr, 3)
    assert arr == [5, 6, 7, 1, 2, 3, 4]
    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate_left(arr, 2)
    assert arr == [3, 4, 5, 6, 7, 1, 2]
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors(colors)
    assert colors == [0, 0, 1, 1, 2, 2]
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert lower_bound([1, 2, 4, 4, 5], 4) == 2
    assert upper_bound([1, 2, 4, 4, 5], 4) == 4
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert first_bad_version(5, lambda v: v >= 4) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated_with_duplicates([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert aggressive_cows([1, 2, 4, 8, 9], 3) == 3
    print("All self-tests passed.")
