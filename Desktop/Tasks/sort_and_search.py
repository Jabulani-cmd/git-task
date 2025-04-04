# Binary search is efficient for sorted lists (O(log n))
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

# Insertion sort is simple and efficient for small/nearly-sorted lists
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

# Linear search is simple and works on any list
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

numbers=[27,-3,4,5,35,2,1,-40,7,18,9,-1,16,100]

# First search (linear) - good for unsorted lists
print("Linear search result:",linear_search(numbers,9))

# Sort the list
sorted_numbers=insertion_sort(numbers.copy())
print("Sorted list:",sorted_numbers)

# Second search (binary) - optimal for sorted lists
print("Binary search result:",binary_search(sorted_numbers,9))

# Real-world use: Binary search is used in databases, filesystems, and any sorted data structure
# where fast lookups are needed (phone books, dictionaries, etc.)