# Merge-Sorts
A detailed setup for Merge Sort, a divide-and-conquer sorting algorithm with guaranteed O(n log n) performance that is stable and comparison-based.

## Problem Description

The **divide and conquer** method involves splitting an array in half recursively, sorting each half, and then merging the sorted halves. With guaranteed O(n log n) performance, merge sort is a **stable, comparison-based** sorting algorithm.

### How It Works
1. **Divide:** Split the array into two halves at the middle index
2. **Conquer:** Recursive sort each half
3. **Combine:** Merge the two sorted halves into one sorted array

### Example
**Input:** `[64, 34, 25, 12, 22, 11, 90]`  
**Output:** `[11, 12, 22, 25, 34, 64, 90]`

## Algorithm Analysis

### Time Complexity
- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n log n) - Always!

### Space Complexity
- **Auxiliary Space:** O(n) for temporary arrays

### Properties
- **Stable** - Maintains relative order of equal elements
- **Not in-place** - Requires extra space
- **Guaranteed performance** - Always O(n log n)
- **Parallelizable** - Halves can be sorted independently

## Complete Python Implementation

### Basic Implementation
```python
def merge_sort(arr):
    """
    Sort array using merge sort
    
    Args:
        arr: Input list to sort
    
    Returns:
        Sorted list (new list, original unchanged)
    """
    if len(arr) <= 1:
        return arr
    
    # DIVIDE step
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # CONQUER step
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays
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
