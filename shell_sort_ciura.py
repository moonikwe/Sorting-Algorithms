def shell_sort_ciura(collection):
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