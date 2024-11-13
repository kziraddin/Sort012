'''Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[]. The functions should put all 0s first, 
then all 1s and all 2s in last.


Input Format There will be two lines of input:


s - the size of the array
ar - the list of numbers that makes up the array

Output Format A single line consisting the list of sorted numbers separated by a single space.


Sample Input
6
0 1 2 2 0 1


Sample Output
0 0 1 1 2 2
'''

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

# Input handling
s = int(input())
ar = list(map(int, input().split()))

# Sort the array
sorted_ar = sort_012(ar, s)

# Output
print(*sorted_ar)