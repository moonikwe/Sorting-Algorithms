
import math
counter = 0
def insertion_sort(collection):
    global counter
    for index in range(1, len(collection)):
        counter += 1
        while 0 < index and collection[index] < collection[index - 1]:
            counter += 1
            collection[index], collection[
                index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection

def bucket_sort(myList, bucket_size):
    global counter
    if(len(myList) == 0):
        print('You don\'t have any elements in array!')

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        counter += 1
        if myList[i] < minValue:
            counter += 1
            minValue = myList[i]
        elif myList[i] > maxValue:
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucket_size) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        buckets[math.floor((myList[i] - minValue) / bucket_size)].append(myList[i])

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        insertion_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])

    return counter