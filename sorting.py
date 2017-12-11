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
#########################################################################
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
#########################################################################
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