"""
Merge Sort - Divide & Conquer Algorithm Implementation
Author: Steven N
Description: Stable O(n log n) sorting algorithm with guaranteed performance
"""

# Import the time module to measure execution time of our sorting functions
import time
# Import random module to generate random test arrays for performance analysis
import random

def merge_sort(arr):
    """
    Sort array using merge sort (divide and conquer)
    This is the standard recursive implementation.
    
    Args:
        arr: Input list to sort
    
    Returns:
        Sorted list (new list, original unchanged)
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n) for temporary arrays
    """
    # Base case: if array has 0 or 1 element, it's already sorted
    # This is the termination condition for our recursion
    if len(arr) <= 1:
        # Return the array as-is (already sorted)
        return arr
    
    # DIVIDE step: Find the middle point of the array
    # Using integer division (//) to get an integer index
    mid = len(arr) // 2
    
    # Recursively sort the left half of the array
    # We pass a copy of the left half by slicing (arr[:mid])
    # This creates a new list containing elements from index 0 to mid-1
    left = merge_sort(arr[:mid])
    
    # Recursively sort the right half of the array
    # We pass a copy of the right half using slicing (arr[mid:])
    # This creates a new list containing elements from index mid to end
    right = merge_sort(arr[mid:])
    
    # CONQUER step: Merge the two sorted halves into one sorted array
    # The merge function combines two sorted lists efficiently
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    This is the key operation in merge sort that combines sorted subarrays.
    
    Args:
        left: Sorted left array
        right: Sorted right array
    
    Returns:
        Merged sorted array
    """
    # Create an empty list to store the merged result
    result = []
    
    # Initialize two pointers, one for left array and one for right array
    # i will traverse the left array, j will traverse the right array
    i = j = 0
    
    # Compare elements from both arrays and add the smaller one to result
    # Continue while both arrays have elements left to compare
    while i < len(left) and j < len(right):
        # If current element in left is less than or equal to current in right
        # Using <= ensures stability (preserves order of equal elements)
        if left[i] <= right[j]:
            # Add the left element to result
            result.append(left[i])
            # Move the left pointer forward
            i += 1
        else:
            # Otherwise, add the right element to result
            result.append(right[j])
            # Move the right pointer forward
            j += 1
    
    # After one array is exhausted, add all remaining elements from left array
    # The extend method adds multiple elements at once
    # left[i:] returns all elements from current i to end
    result.extend(left[i:])
    
    # Add all remaining elements from right array
    # right[j:] returns all elements from current j to end
    result.extend(right[j:])
    
    # Return the fully merged and sorted array
    return result


def merge_sort_inplace(arr, temp=None, left=0, right=None):
    """
    In-place version of merge sort (still uses O(n) extra space for merging)
    This version modifies the original array instead of creating new ones.
    
    Args:
        arr: Input list to sort (will be modified)
        temp: Temporary array for merging
        left: Left index of subarray
        right: Right index of subarray
    
    Returns:
        Sorted list (same reference)
    """
    # Initialize on first call (when right is None)
    if right is None:
        # Set right to the last index of the array
        right = len(arr) - 1
        # Create a temporary array of the same size, filled with zeros
        temp = [0] * len(arr)
    
    # Only proceed if left index is less than right index
    # This means we have at least two elements to sort
    if left < right:
        # Calculate middle point using integer division
        mid = (left + right) // 2
        
        # Recursively sort the left half (from left to mid)
        # Pass the same arr, temp, and update indices
        merge_sort_inplace(arr, temp, left, mid)
        
        # Recursively sort the right half (from mid+1 to right)
        # Pass the same arr, temp, and update indices
        merge_sort_inplace(arr, temp, mid + 1, right)
        
        # Merge the two sorted halves back into the original array
        # This uses the temporary array for merging
        merge_inplace(arr, temp, left, mid, right)
    
    # Return the sorted array (same reference as input)
    return arr


def merge_inplace(arr, temp, left, mid, right):
    """
    Merge two sorted subarrays arr[left..mid] and arr[mid+1..right]
    using temporary array. This modifies the original array directly.
    """
    # Copy both subarrays into the temporary array
    # We copy from left to right inclusive
    for i in range(left, right + 1):
        # Each element from original array goes to same index in temp
        temp[i] = arr[i]
    
    # Initialize three pointers:
    # i points to current position in left subarray (starts at left)
    i = left
    
    # j points to current position in right subarray (starts at mid+1)
    j = mid + 1
    
    # k points to current position in merged array (starts at left)
    k = left
    
    # Merge back to original array while both subarrays have elements
    while i <= mid and j <= right:
        # Compare elements from left and right subarrays
        if temp[i] <= temp[j]:
            # If left element is smaller, put it in original array
            arr[k] = temp[i]
            # Move left pointer forward
            i += 1
        else:
            # If right element is smaller, put it in original array
            arr[k] = temp[j]
            # Move right pointer forward
            j += 1
        # Move merged array pointer forward
        k += 1
    
    # Copy remaining elements from left subarray (if any)
    # This loop runs only if there are leftover elements in left
    while i <= mid:
        # Copy each remaining left element to original array
        arr[k] = temp[i]
        # Move both pointers forward
        i += 1
        k += 1
    
    # Elements from right subarray are already in place
    # No need to copy them explicitly because they're already in correct positions
    # The while loop above and the merge condition ensure this


def merge_sort_detailed(arr, depth=0):
    """
    Detailed version with step-by-step output for learning
    This helps visualize the recursive divide-and-conquer process.
    
    Args:
        arr: Input list to sort
        depth: Recursion depth for indentation
    
    Returns:
        Sorted list
    """
    # Create indentation string based on recursion depth
    # More depth = more indentation, making the recursion tree visible
    indent = "  " * depth
    
    # Print current call with the array being processed
    print(f"{indent}merge_sort({arr})")
    
    # Base case: if array length is 0 or 1, it's already sorted
    if len(arr) <= 1:
        # Print base case reached
        print(f"{indent}→ Base case: {arr}")
        # Return the array unchanged
        return arr
    
    # Calculate middle index using  division
    mid = len(arr) // 2
    
    # Print how we're splitting the array
    print(f"{indent}Split at index {mid}: {arr[:mid]} | {arr[mid:]}")
    
    # Recursively sort left half with increased depth
    left = merge_sort_detailed(arr[:mid], depth + 1)
    
    # Recursively sort right half with increased depth
    right = merge_sort_detailed(arr[mid:], depth + 1)
    
    # Print that we're now merging the sorted halves
    print(f"{indent}Merging {left} and {right}")
    
    # Merge the sorted halves using detailed merge function
    result = merge_detailed(left, right, depth)
    
    # Print the result of this merge
    print(f"{indent}→ Result: {result}")
    
    # Return the merged result
    return result


def merge_detailed(left, right, depth=0):
    """Detailed merge with step-by-step output for learning"""
    # Create indentation string based on depth plus one extra level
    indent = "  " * (depth + 1)
    
    # Initialize empty list for result
    result = []
    
    # Initialize pointers for left and right arrays
    i = j = 0
    
    # Initialize step counter for the merge process
    step = 1
    
    # Print header for merge process
    print(f"{indent}Merge process:")
    
    # Continue while both arrays have elements to compare
    while i < len(left) and j < len(right):
        # Compare current elements from left and right
        if left[i] <= right[j]:
            # If left element is smaller or equal, take from left
            print(f"{indent}  Step {step}: {left[i]} <= {right[j]} → take from left")
            # Add left element to result
            result.append(left[i])
            # Move left pointer forward
            i += 1
        else:
            # If right element is smaller, take from right
            print(f"{indent}  Step {step}: {left[i]} > {right[j]} → take from right")
            # Add right element to result
            result.append(right[j])
            # Move right pointer forward
            j += 1
        
        # Increment step counter
        step += 1
        
        # Print current state of result after this step
        print(f"{indent}    Current result: {result}")
    
    # Add remaining elements from left array (if any)
    while i < len(left):
        # Print that we're adding remaining left element
        print(f"{indent}  Step {step}: Add remaining left element {left[i]}")
        # Add the left element to result
        result.append(left[i])
        # Move left pointer forward
        i += 1
        # Increment step counter
        step += 1
        # Print current state of result
        print(f"{indent}    Current result: {result}")
    
    # Add remaining elements from right array (if any)
    while j < len(right):
        # Print that we're adding remaining right element
        print(f"{indent}  Step {step}: Add remaining right element {right[j]}")
        # Add the right element to result
        result.append(right[j])
        # Move right pointer forward
        j += 1
        # Increment step counter
        step += 1
        # Print current state of result
        print(f"{indent}    Current result: {result}")
    
    # Return the fully merged result
    return result


def merge_sort_bottom_up(arr):
    """
    Bottom-up (iterative) merge sort
    This version avoids recursion by iteratively merging larger and larger subarrays.
    
    Args:
        arr: Input list to sort
    
    Returns:
        Sorted list
    """
    # Get the length of the input array
    n = len(arr)
    
    # Create a copy of the array to avoid modifying the original
    result = arr.copy()
    
    # Start with subarrays of size 1 (already sorted)
    width = 1
    
    # Print header for bottom-up approach
    print("\nBottom-up merge sort:")
    
    # Continue until subarray size is less than array length
    # When width >= n, we've merged the entire array
    while width < n:
        # Print current merge pass with subarray size
        print(f"\nMerging subarrays of size {width}:")
        
        # Merge subarrays in pairs
        # i represents the start index of each pair of subarrays
        for i in range(0, n, 2 * width):
            # Calculate left boundary of first subarray
            left = i
            
            # Calculate middle (end of first subarray, start of second)
            # Use min to handle the last partial subarray
            mid = min(i + width, n)
            
            # Calculate right boundary of second subarray
            # Use min to handle array end
            right = min(i + 2 * width, n)
            
            # Only merge if there are two subarrays (mid < right)
            if mid < right:
                # Print which subarrays we're merging
                print(f"  Merging [{left}:{mid}] and [{mid}:{right}]")
                # Merge the two subarrays and update result
                # Slicing extracts the subarrays, merge_bottom_up combines them
                result[left:right] = merge_bottom_up(result[left:mid], result[mid:right])
        
        # Double the subarray size for next pass
        width *= 2
    
    # Return the fully sorted array
    return result


def merge_bottom_up(left, right):
    """Merge helper for bottom-up version"""
    # Create empty list for result
    result = []
    
    # Initialize pointers for left and right arrays
    i = j = 0
    
    # Compare elements from both arrays while both have elements
    while i < len(left) and j < len(right):
        # If left element is smaller or equal, take from left
        if left[i] <= right[j]:
            # Add left element to result
            result.append(left[i])
            # Move left pointer forward
            i += 1
        else:
            # Otherwise, take from right
            result.append(right[j])
            # Move right pointer forward
            j += 1
    
    # Add any remaining elements from left array
    result.extend(left[i:])
    
    # Add any remaining elements from right array
    result.extend(right[j:])
    
    # Return the merged result
    return result


def merge_sort_parallel(arr, threshold=1000):
    """
    Simple parallel version using recursion
    
    Note: This is a conceptual example. For true parallel sorting,
    use multiprocessing or specialized libraries.
    
    Args:
        arr: Input list to sort
        threshold: Size below which to sort sequentially
    
    Returns:
        Sorted list
    """
    # If array is small enough, sort running
    if len(arr) <= threshold:
        # Use standard merge sort for small arrays
        return merge_sort(arr)
    
    # Calculate middle index
    mid = len(arr) // 2
    
    # In practice, these would run in parallel on different processors
    # Sort left half recursively with same threshold
    left = merge_sort_parallel(arr[:mid], threshold)
    
    # Sort right half recursively with same threshold
    right = merge_sort_parallel(arr[mid:], threshold)
    
    # Merge the sorted halves and return
    return merge(left, right)


def count_inversions(arr):
    """
    Count inversions in array using merge sort
    
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j]
    This is a classic application of merge sort.
    
    Args:
        arr: Input array
    
    Returns:
        Number of inversions
    """
    def merge_count(arr, temp, left, mid, right):
        """
        Merge two sorted subarrays and count inversions
        Returns the merged array and inversion count
        """
        # Initialize pointers:
        # i for left subarray, j for right subarray, k for temp array
        i = left
        j = mid + 1
        k = left
        
        # Initialize inversion counter
        inv_count = 0
        
        # Merge while both subarrays have elements
        while i <= mid and j <= right:
            # If left element is smaller or equal, no inversion
            if arr[i] <= arr[j]:
                # Copy left element to temp
                temp[k] = arr[i]
                # Move left pointer forward
                i += 1
            else:
                # Left element is greater than right element
                # This creates inversions: all remaining left elements
                # are greater than this right element
                temp[k] = arr[j]
                # Count inversions: number of elements remaining in left
                inv_count += (mid - i + 1)
                # Move right pointer forward
                j += 1
            # Move temp pointer forward
            k += 1
        
        # Copy remaining elements from left subarray
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        # Copy remaining elements from right subarray
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # Copy merged elements back to original array
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        # Return inversion count for this merge
        return inv_count
    
    def merge_sort_count(arr, temp, left, right):
        """
        Recursive merge sort that counts inversions
        """
        # Initialize inversion counter
        inv_count = 0
        
        # Only proceed if we have more than one element
        if left < right:
            # Find middle point
            mid = (left + right) // 2
            
            # Count inversions in left half
            inv_count += merge_sort_count(arr, temp, left, mid)
            
            # Count inversions in right half
            inv_count += merge_sort_count(arr, temp, mid + 1, right)
            
            # Count inversions during merge
            inv_count += merge_count(arr, temp, left, mid, right)
        
        # Return total inversion count
        return inv_count
    
    # Create a copy of the array to avoid modifying original
    arr_copy = arr.copy()
    
    # Create temporary array of same size
    temp = [0] * len(arr_copy)
    
    # Start the recursive inversion counting
    return merge_sort_count(arr_copy, temp, 0, len(arr_copy) - 1)


def analyze_sorting_algorithm(arr, func, name):
    """Analyze performance of a sorting algorithm"""
    # Create a copy of the array to avoid modifying the original
    # This make sures each algorithm works on the same input
    arr_copy = arr.copy()
    
    # Record start time using high-precision timer
    start = time.time()
    
    # Execute the sorting function on the array copy
    result = func(arr_copy)
    
    # Record end time
    end = time.time()
    
    # Print analysis results
    print(f"\n{name}:")
    # Calculate elapsed time in milliseconds (multiply by 1000)
    print(f"  Time: {(end - start) * 1000:.4f} ms")
    
    # If array is small enough, print the sorted result
    if len(result) <= 20:
        print(f"  Result: {result}")
    
    # Return the sorted result (though we don't use it)
    return result


def generate_test_arrays():
    """Generate test arrays for performance analysis"""
    # Return dictionary of different array types for testing
    return {
        # Random array: elements randomly distributed
        "Random": [random.randint(1, 1000) for _ in range(20)],
        
        # Already sorted array: best-case scenario
        "Sorted": list(range(20)),
        
        # Reverse sorted array: worst-case for some algorithms
        "Reverse Sorted": list(range(20, 0, -1)),
        
        # Array with many duplicates: tests stability
        "Many Duplicates": [random.randint(1, 5) for _ in range(20)],
        
        # Small fixed array for demonstration
        "Small": [5, 2, 8, 1, 9, 3, 7, 4, 6]
    }


# Example usage - only runs if script is executed directly
if __name__ == "__main__":
    # Print main header
    print("=" * 60)
    print("MERGE SORT ALGORITHM DEMONSTRATION")
    print("=" * 60)
    
    # Basic example array for demonstration
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {arr}")
    
    # Sort the array using standard merge sort
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}")
    
    # Demonstrate the merge process with two sorted arrays
    print("\n--- Merge Process Demonstration ---")
    left_example = [11, 12, 25]
    right_example = [22, 34, 64]
    print(f"Merging: {left_example} and {right_example}")
    print(f"Result:  {merge(left_example, right_example)}")
    
    # Detailed walkthrough showing recursion tree
    print("\n" + "=" * 60)
    print("DETAILED WALKTHROUGH")
    print("=" * 60)
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort_detailed(test_arr)
    
    # Test different versions of merge sort
    print("\n" + "=" * 60)
    print("ALGORITHM VARIATIONS")
    print("=" * 60)
    
    # Generate various test arrays
    test_arrays = generate_test_arrays()
    
    # Test each array type with different merge sort versions
    for arr_name, test_arr in test_arrays.items():
        print(f"\n{arr_name} Array:")
        
        # Test standard version (returns new array)
        analyze_sorting_algorithm(test_arr, merge_sort, "Standard")
        
        # Test in-place version (modifies array)
        # Use lambda to create a copy since in-place modifies
        analyze_sorting_algorithm(test_arr, lambda a: merge_sort_inplace(a.copy()), "In-place")
        
        # Test bottom-up (iterative) version
        analyze_sorting_algorithm(test_arr, merge_sort_bottom_up, "Bottom-up")
    
    # Inversion count example
    print("\n" + "=" * 60)
    print("INVERSION COUNT EXAMPLE")
    print("=" * 60)
    
    # Array to show inversion counting
    inv_arr = [2, 4, 1, 3, 5]
    print(f"Array: {inv_arr}")
    
    # Count inversions in the array
    inv_count = count_inversions(inv_arr.copy())
    print(f"Number of inversions: {inv_count}")
    
    # Verify stability 
    print("\n" + "=" * 60)
    print("STABILITY DEMONSTRATION")
    print("=" * 60)
    
    # Create array with duplicate values but different identities
    # Each element is a tuple (value, id) to track original order
    pairs = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
    print(f"Original pairs: {pairs}")
    
    def sort_by_first(pairs):
        """
        Sort list of pairs by first element, maintaining stability
        This demonstrates merge sort's stable sorting property
        """
        # Base case: if array has 0 or 1 element, it's already sorted
        if len(pairs) <= 1:
            return pairs
        
        # Find middle point
        mid = len(pairs) // 2
        
        # Recursively sort left and right halves
        left = sort_by_first(pairs[:mid])
        right = sort_by_first(pairs[mid:])
        
        # Merge while maintaining stability
        result = []
        i = j = 0
        
        # Merge the two sorted halves
        while i < len(left) and j < len(right):
            # Use <= to ensure stability - if equal, take from left first
            # This keeps the original order of equal elements
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    # Sort the pairs by first element
    sorted_pairs = sort_by_first(pairs)
    print(f"Sorted pairs (stable): {sorted_pairs}")
    print("Note: (2,'a') appears before (2,'c') - original order preserved")
    
    # Print key insights about merge sort
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
