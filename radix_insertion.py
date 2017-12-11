counter = 0 #Variable to count the number of accesses in the array
def insertion_sort(arr, exp1):
    n = len(arr)
    global counter

    for i in range(1, n):
        key = arr[i] #A variable key will hold the value of the first element in the array
        
        j = i-1
        while j >=0 and ((key)%exp1) < ((arr[j])%exp1) : #Insertion Algo is applied to each place value digit of each elemt in the array for every iteration
                counter += 1 #Increases the counter for how many times the element in the array is accessed
                arr[j+1] = arr[j] #If the condition satisfies, the value is moved and changed
                j -= 1
        counter += 1 #Increases the counter for how many times the element in the array is accessed (for the failed)
        arr[j+1] = key #Changing of the value of the array index upon changing after comparison

def radix_insertion(arr):
    global counter
    counter = 0

    max1 = max(arr) #This will look for the largest number in the array (to know the max length of the input in the array)                                 
    exp = 1 #This will serve as the multiplier for each position in every element of the array

    while max1/exp > 0:
        insertion_sort(arr,exp) #The array and the multiplier that will be used for the insertion algorithm is passed
        exp *= 10 #Each iteration, multiplier is multiplied by 10 to represent the place value of each input that will be sorted
    return counter