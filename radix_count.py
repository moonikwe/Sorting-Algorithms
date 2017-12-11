counter = 0 # Variable to  count the number of accesses in the array                                    
def counting_sort(arr, exp1):
    n = len(arr)
    global counter

    count = [0] * (10) #initalize count array as 0
    output = [0] * (n) # The output array elements that will have sorted arr

    for i in range(0, n):  # Store count of occurrences in count[]
        index = int((arr[i]/exp1))
        counter += 1                         
        count[ (index)%10 ] += 1                    

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]                     
 
    # Build the output array
    i = n-1
    while i>=0:
        index = int((arr[i]/exp1))
        output[ count[ (index)%10 ] - 1] = arr[i]   
        count[ (index)%10 ] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i] #Stores the output back to the original array
 
def radix_count(arr):
    global counter
    counter = 0

    # Find the maximum number to know number of digits
    max1 = max(arr)                                
                              
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1  
    while max1/exp > 0:
        counting_sort(arr,exp)                      
        exp *= 10              
    return counter