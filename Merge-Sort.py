"""
Merge Sort - Divide & Conquer Algorithm Implementation
Author: Steven N
Description: Stable O(n log n) sorting algorithm with guaranteed performance
"""

import time
import random

def merge_sort(arr):
    """
    Sort array using merge sort (divide and conquer)
    
    Args:
        arr: Input list to sort
    
    Returns:
        Sorted list (new list, original unchanged)
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n) for temporary arrays
    """
    # Base case: array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # DIVIDE step: Find the middle point
    mid = len(arr) // 2
    
    # Recursively sort left and right halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # CONQUER step: Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    
    Args:
        left: Sorted left array
        right: Sorted right array
    
    Returns:
        Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort_inplace(arr, temp=None, left=0, right=None):
    """
    In-place version of merge sort (still uses O(n) extra space for merging)
    
    Args:
        arr: Input list to sort (will be modified)
        temp: Temporary array for merging
        left: Left index of subarray
        right: Right index of subarray
    
    Returns:
        Sorted list (same reference)
    """
    if right is None:
        right = len(arr) - 1
        temp = [0] * len(arr)
    
    if left < right:
        mid = (left + right) // 2
        
        # Recursively sort halves
        merge_sort_inplace(arr, temp, left, mid)
        merge_sort_inplace(arr, temp, mid + 1, right)
        
        # Merge the sorted halves
        merge_inplace(arr, temp, left, mid, right)
    
    return arr


def merge_inplace(arr, temp, left, mid, right):
    """
    Merge two sorted subarrays arr[left..mid] and arr[mid+1..right]
    using temporary array
    """
    # Copy both subarrays to temp
    for i in range(left, right + 1):
        temp[i] = arr[i]
    
    i = left      # Index for left subarray
    j = mid + 1   # Index for right subarray
    k = left      # Index for merged array
    
    # Merge back to original array
    while i <= mid and j <= right:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1
    
    # Copy remaining elements from left subarray
    while i <= mid:
        arr[k] = temp[i]
        i += 1
        k += 1
    
    # Elements from right subarray are already in place


def merge_sort_detailed(arr, depth=0):
    """
    Detailed version with step-by-step output for learning
    
    Args:
        arr: Input list to sort
        depth: Recursion depth for indentation
    
    Returns:
        Sorted list
    """
    indent = "  " * depth
    
    print(f"{indent}merge_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}→ Base case: {arr}")
        return arr
    
    mid = len(arr) // 2
    print(f"{indent}Split at index {mid}: {arr[:mid]} | {arr[mid:]}")
    
    left = merge_sort_detailed(arr[:mid], depth + 1)
    right = merge_sort_detailed(arr[mid:], depth + 1)
    
    print(f"{indent}Merging {left} and {right}")
    result = merge_detailed(left, right, depth)
    print(f"{indent}→ Result: {result}")
    
    return result


def merge_detailed(left, right, depth=0):
    """Detailed merge with step-by-step output"""
    indent = "  " * (depth + 1)
    
    result = []
    i = j = 0
    step = 1
    
    print(f"{indent}Merge process:")
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            print(f"{indent}  Step {step}: {left[i]} <= {right[j]} → take from left")
            result.append(left[i])
            i += 1
        else:
            print(f"{indent}  Step {step}: {left[i]} > {right[j]} → take from right")
            result.append(right[j])
            j += 1
        step += 1
        print(f"{indent}    Current result: {result}")
    
    # Add remaining elements
    while i < len(left):
        print(f"{indent}  Step {step}: Add remaining left element {left[i]}")
        result.append(left[i])
        i += 1
        step += 1
        print(f"{indent}    Current result: {result}")
    
    while j < len(right):
        print(f"{indent}  Step {step}: Add remaining right element {right[j]}")
        result.append(right[j])
        j += 1
        step += 1
        print(f"{indent}    Current result: {result}")
    
    return result


def merge_sort_bottom_up(arr):
    """
    Bottom-up (iterative) merge sort
    
    Args:
        arr: Input list to sort
    
    Returns:
        Sorted list
    """
    n = len(arr)
    result = arr.copy()
    width = 1
    
    print("\nBottom-up merge sort:")
    
    while width < n:
        print(f"\nMerging subarrays of size {width}:")
        
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)
            
            if mid < right:
                print(f"  Merging [{left}:{mid}] and [{mid}:{right}]")
                result[left:right] = merge_bottom_up(result[left:mid], result[mid:right])
        
        width *= 2
    
    return result


def merge_bottom_up(left, right):
    """Merge helper for bottom-up version"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_parallel(arr, threshold=1000):
    """
    Simple parallel version using recursion
    
    Note: This is a conceptual example. For true parallel sorting,
    use multiprocessing or specialized libraries.
    """
    if len(arr) <= threshold:
        return merge_sort(arr)
    
    mid = len(arr) // 2
    
    # In practice, these would run in parallel
    left = merge_sort_parallel(arr[:mid], threshold)
    right = merge_sort_parallel(arr[mid:], threshold)
    
    return merge(left, right)


def count_inversions(arr):
    """
    Count inversions in array using merge sort
    
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j]
    
    Args:
        arr: Input array
    
    Returns:
        Number of inversions
    """
    def merge_count(arr, temp, left, mid, right):
        i = left      # Index for left subarray
        j = mid + 1   # Index for right subarray
        k = left      # Index for merged array
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                # There are mid - i inversions because all elements
                # from i to mid are greater than arr[j]
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_count(arr, temp, left, mid)
            inv_count += merge_sort_count(arr, temp, mid + 1, right)
            inv_count += merge_count(arr, temp, left, mid, right)
        return inv_count
    
    arr_copy = arr.copy()
    temp = [0] * len(arr_copy)
    return merge_sort_count(arr_copy, temp, 0, len(arr_copy) - 1)


def analyze_sorting_algorithm(arr, func, name):
    """Analyze performance of a sorting algorithm"""
    arr_copy = arr.copy()
    
    start = time.time()
    result = func(arr_copy)
    end = time.time()
    
    print(f"\n{name}:")
    print(f"  Time: {(end - start) * 1000:.4f} ms")
    if len(result) <= 20:
        print(f"  Result: {result}")
    
    return result


def generate_test_arrays():
    """Generate test arrays for performance analysis"""
    return {
        "Random": [random.randint(1, 1000) for _ in range(20)],
        "Sorted": list(range(20)),
        "Reverse Sorted": list(range(20, 0, -1)),
        "Many Duplicates": [random.randint(1, 5) for _ in range(20)],
        "Small": [5, 2, 8, 1, 9, 3, 7, 4, 6]
    }


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("MERGE SORT ALGORITHM DEMONSTRATION")
    print("=" * 60)
    
    # Basic example
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {arr}")
    
    # Sort the array
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}")
    
    # Demonstrate the merge process
    print("\n--- Merge Process Demonstration ---")
    left_example = [11, 12, 25]
    right_example = [22, 34, 64]
    print(f"Merging: {left_example} and {right_example}")
    print(f"Result:  {merge(left_example, right_example)}")
    
    # Detailed walkthrough
    print("\n" + "=" * 60)
    print("DETAILED WALKTHROUGH")
    print("=" * 60)
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort_detailed(test_arr)
    
    # Test different versions
    print("\n" + "=" * 60)
    print("ALGORITHM VARIATIONS")
    print("=" * 60)
    
    test_arrays = generate_test_arrays()
    
    for arr_name, test_arr in test_arrays.items():
        print(f"\n{arr_name} Array:")
        
        # Test different versions
        analyze_sorting_algorithm(test_arr, merge_sort, "Standard")
        analyze_sorting_algorithm(test_arr, lambda a: merge_sort_inplace(a.copy()), "In-place")
        analyze_sorting_algorithm(test_arr, merge_sort_bottom_up, "Bottom-up")
    
    # Inversion count example
    print("\n" + "=" * 60)
    print("INVERSION COUNT EXAMPLE")
    print("=" * 60)
    
    inv_arr = [2, 4, 1, 3, 5]
    print(f"Array: {inv_arr}")
    inv_count = count_inversions(inv_arr.copy())
    print(f"Number of inversions: {inv_count}")
    
    # Verify stability
    print("\n" + "=" * 60)
    print("STABILITY DEMONSTRATION")
    print("=" * 60)
    
    # Create array with duplicate values but different identities
    pairs = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
    print(f"Original pairs: {pairs}")
    
    def sort_by_first(pairs):
        if len(pairs) <= 1:
            return pairs
        mid = len(pairs) // 2
        left = sort_by_first(pairs[:mid])
        right = sort_by_first(pairs[mid:])
        
        # Merge while maintaining stability
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    sorted_pairs = sort_by_first(pairs)
    print(f"Sorted pairs (stable): {sorted_pairs}")
    print("Note: (2,'a') appears before (2,'c') - original order preserved")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)
    print("""
    1. Guaranteed O(n log n) performance regardless of input
    2. Stable sorting algorithm - maintains relative order of equal elements
    3. Not in-place - requires O(n) extra space
    4. Divide and conquer approach: divide, recursively sort, merge
    5. Recurrence relation: T(n) = 2T(n/2) + O(n) → O(n log n)
    6. Excellent for linked lists and external sorting
    """)
