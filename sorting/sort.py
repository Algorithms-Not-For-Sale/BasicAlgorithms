'''
* Time Complexity: O(n*2)
* Auxiliary Space: O(1)
* Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it 
takes minimum time (Order of n) when elements are already sorted.
* Algorithmic Paradigm: Incremental Approach
* Sorting In Place: Yes
* Stable: Yes
* Online: Yes
* Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost 
sorted, only few elements are misplaced in complete big array.
'''

def insertsort(arr):
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1

        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                
        arr[j+1] = key 
    
    return arr