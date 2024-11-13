# Sort Array of 0s, 1s, and 2s

## Problem Description

This program solves the problem of sorting an array consisting of only 0s, 1s, and 2s. The goal is to arrange the array so that all 0s come first, followed by all 1s, and then all 2s.

## Algorithm: Dutch National Flag

The solution uses the Dutch National Flag algorithm, also known as three-way partitioning. This algorithm sorts the array in a single pass, making it highly efficient.

### Key Points:
- Time Complexity: O(n)
- Space Complexity: O(1)
- In-place sorting

## Implementation

```python
def sort_012(arr, n):
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
