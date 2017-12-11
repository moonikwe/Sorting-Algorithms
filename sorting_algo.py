#This is an MP on a comparison of Sorting Algorithms 

# Python program for implementation of Selection
"""def selection_sort(alist):
	counter = 0
	for fillslot in range(len(alist)-1,0,-1):
   		positionOfMax = 0
   		for location in range(1,fillslot+1):
   			if alist[location] > alist[positionOfMax]:
   				positionOfMax = location
   				counter+=1

   		temp = alist[fillslot]
   		alist[fillslot] = alist[positionOfMax]
   		alist[positionOfMax] = temp

	return counter"""
#####################################################
def selection_sort(collection):
    counter = 0
    length = len(collection)
    for i in range(length):
        least = i
        for k in range(i + 1, length):
            counter += 1
            if collection[k] < collection[least]:
                least = k
                counter += 1
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
    return counter
#####################################################
def bubble_sort(collection):
    counter = 0;
    for passnum in range(len(collection)-1,0,-1):
        for i in range(passnum):
            counter += 1
            if collection[i] > collection[i+1]:
                counter += 1
                temp = collection[i]
                collection[i] = collection[i+1]
                collection[i+1] = temp

    return counter
#####################################################
def insertion_sort(collection):
    counter = 0;
    for index in range(1, len(collection)):
        counter += 1
        while 0 < index and collection[index] < collection[index - 1]:
            counter += 1
            collection[index], collection[
                index - 1] = collection[index - 1], collection[index]
            index -= 1

    return counter

#####################################################
def shell_sort_shell(arr):
    counter = 0

    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(gap,n):
 
            counter += 1
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                counter += 1
                arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2
    return counter

#####################################################
def shell_sort(collection):
    counter = 0
    
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            counter += 1
            while j >= gap and collection[j - gap] > temp:
                counter += 1
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1

    return counter

#####################################################
def bucket_sort( collection ):
  counter = 0
  # get hash codes
  code = hashing( collection )
  counter += code[2]
  buckets = [list() for _ in range( code[1] )]
  for i in collection:
    x = re_hashing( i, code )
    buck = buckets[x]
    buck.append( i )
 
  for bucket in buckets:
    counter += insertion_sort( bucket )
 
  ndx = 0
  # merge the buckets: O(n)
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      collection[ndx] = v
      ndx += 1
  return counter
#####################################################
import math
 
def hashing( A ):
  counter = 0
  result = []
  m = A[0]
  for i in range( 1, len( A ) ):
    counter += 1
    if ( m < A[i] ):
      counter += 1
      m = A[i]

  result.append(m)
  result.append(int( math.sqrt( len( A ) )))
  result.append(counter)
  return result

#####################################################
def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )

#####################################################
# Python program for implementation of Radix Sort
 
# A function to do counting sort of arr[] according to
# the digit represented by exp.
def counting_sort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]//exp1)
        count[ (index)%10 ] += 1
 
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]
 
    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]//exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

#####################################################
# Method to do Radix Sort
def radix_sort(collection):
 
    # Find the maximum number to know number of digits
    maximum = max(collection)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exponent = 1
    while maximum/exponent > 0:
        counting_sort(collection, exponent)
        exponent *= 10
    return collection
#####################################################
def merge_sort(xs):
    counter = 0
    unit = 1
    while unit <= len(xs):
        h = 0
        for h in range(0, len(xs), unit * 2):
            l, r = h, min(len(xs), h + 2 * unit)
            mid = h + unit
            # merge xs[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                counter += 1
                if xs[p] < xs[q]: 
                  p += 1
                  counter += 1
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1

        unit *= 2
    
    return counter
#####################################################
def quicksort(array):
    counter = 0
    indexes_stack = list()
    idx = (0, len(array) - 1)
    indexes_stack.append(idx)
    for idx in indexes_stack:
        elem_idx = idx[0]
        pivot_idx = idx[1]
        while pivot_idx > elem_idx:
            counter += 1
            pivot = array[pivot_idx]
            elem = array[elem_idx]
            if elem > pivot:
                counter += 1
                array[pivot_idx] = elem
                array[elem_idx] = array[pivot_idx - 1]
                array[pivot_idx - 1] = pivot
                pivot_idx -= 1
            else:
                elem_idx += 1

        boundar_low = idx[0]
        boundar_high = idx[1]
        if pivot_idx > 1 and boundar_low < pivot_idx - 1:
            counter += 1
            indexes_stack.append((boundar_low, pivot_idx - 1))
        if pivot_idx < len(array) -1 and pivot_idx + 1 < boundar_high:
            counter += 1
            indexes_stack.append((pivot_idx + 1, boundar_high))

    return counter
#####################################################
#collection = [54,26,93,17,77,31,44,55,20]
#print("Unsorted ", collection)
#print("Sorted ", merge_sort(collection))