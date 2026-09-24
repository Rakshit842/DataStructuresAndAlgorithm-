# 1.Given a number n, count the total number of digits in the number.
def count_digits_iterative(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        n //= 10
        count += 1
    return count

# 2.Given an integer n, reverse its digits.
def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10          # Get last digit
        reverse = reverse * 10 + digit
        n = n // 10             # Remove last digit

    return reverse

# 3.Given an integer n, check whether the number is a palindrome
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse

n = 121
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")

# 4.Given an integer n, check whether it is an Armstrong number.
def is_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n = n // 10

    return original == total

# 5.Given a decimal number n, convert it into its binary representation.
def decimal_to_binary(n):
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary

# 6.Print Alternate Elements of an Array
def print_alternate(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=" ")

arr = [10, 20, 30, 40, 50, 60]

print("Alternate elements are:")
print_alternate(arr)

# 7.Calculate Sum and Product of Array Elements
def sum_and_product(arr):
    total_sum = 0
    product = 1

    for num in arr:
        total_sum += num
        product *= num

    print("Sum =", total_sum)
    print("Product =", product)

# 8. Count Occurrences of a Target Number in an Array
def count_occurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count

# 9.Check if an Array is Sorted Forward, Backward or Not at All
def check_array_order(arr):
    ascending = True
    descending = True

    for i in range(len(arr) - 1):

        # Check ascending order
        if arr[i] > arr[i + 1]:
            ascending = False

        # Check descending order
        if arr[i] < arr[i + 1]:
            descending = False

    if ascending:
        return "Sorted Forward (Ascending)"
    elif descending:
        return "Sorted Backward (Descending)"
    else:
        return "Not Sorted"
    
# 10.Find distinct elements
def find_distinct(arr):
    distinct = []

    for num in arr:
        if num not in distinct:
            distinct.append(num)

    return distinct

# 11.Check if Two Elements Exist with a Sum Equal to a Target Value
def has_pair_with_sum(arr, target):
    seen = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            return True

        seen.add(num)

    return False

# 12.Find the Missing Number
def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)

    return total_sum - array_sum

# 13.Find Second Smallest and Second Largest Element in an array
def find_second_smallest_largest(arr):

    # Remove duplicate elements
    unique = list(set(arr))

    # Array should have at least 2 unique elements
    if len(unique) < 2:
        return "Not enough elements"

    unique.sort()

    second_smallest = unique[1]
    second_largest = unique[-2]

    return second_smallest, second_largest

# 14.Sum Of Max And Min
def sum_of_max_and_min(arr):

    maximum = max(arr)
    minimum = min(arr)

    return maximum + minimum

# 15.Find the duplicate in an array of N+1 integers
def find_duplicate(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return num

        seen.add(num)

    return -1

# 16.Find the Most Frequent Element in a List
def most_frequent_element(arr):
    frequency = {}

    # Count frequency of each element
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find element with maximum frequency
    max_count = 0
    most_frequent = None

    for key, value in frequency.items():
        if value > max_count:
            max_count = value
            most_frequent = key

    return most_frequent

# 17.Find the Missing Number in an Array
def find_missing_number(arr, n):

    # Sum of first n natural numbers
    expected_sum = n * (n + 1) // 2

    # Sum of array elements
    actual_sum = sum(arr)

    # Missing number
    return expected_sum - actual_sum

# 18.Move Zeroes
def move_zeroes(arr):
    result = []

    # Add non-zero elements
    for num in arr:
        if num != 0:
            result.append(num)

    # Count zeroes
    zero_count = arr.count(0)

    # Add zeroes at the end
    for i in range(zero_count):
        result.append(0)

    return result

# 19.Plus One
def plus_one(digits):

    # Traverse from last digit
    for i in range(len(digits) - 1, -1, -1):

        # If digit is less than 9, add 1 and return
        if digits[i] < 9:
            digits[i] += 1
            return digits

        # If digit is 9, make it 0
        digits[i] = 0

    # If all digits were 9
    return [1] + digits

# 20.Rotate array by K
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    rotated = arr[-k:] + arr[:-k]
    return rotated
