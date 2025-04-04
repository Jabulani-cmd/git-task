def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left)and j<len(right):
            if len(left[i])>=len(right[j]):
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
words1=["apple","banana","grapefruit","pear","kiwi","watermelon","orange","blueberry","strawberry","melon"]
words2=["Python","JavaScript","Java","C++","TypeScript","Ruby","Go","Swift","Kotlin","Rust"]
words3=["elephant","giraffe","lion","tiger","zebra","rhinoceros","hippopotamus","kangaroo","monkey","cheetah"]
print("Original lists:")
print("List 1:",words1)
print("List 2:",words2)
print("List 3:",words3)
merge_sort(words1)
merge_sort(words2)
merge_sort(words3)
print("\nSorted by length (longest to shortest):")
print("List 1:",words1)
print("List 2:",words2)
print("List 3:",words3)