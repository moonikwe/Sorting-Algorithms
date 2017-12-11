def quick_sort(collection):
    counter = 0
    indexes_stack = list()
    idx = (0, len(collection) - 1)
    indexes_stack.append(idx)
    for idx in indexes_stack:
        elem_idx = idx[0]
        pivot_idx = idx[1]
        while pivot_idx > elem_idx:
            counter += 1
            pivot = collection[pivot_idx]
            elem = collection[elem_idx]
            if elem > pivot:
                counter += 1
                collection[pivot_idx] = elem
                collection[elem_idx] = collection[pivot_idx - 1]
                collection[pivot_idx - 1] = pivot
                pivot_idx -= 1
            else:
                elem_idx += 1

        boundar_low = idx[0]
        boundar_high = idx[1]
        if pivot_idx > 1 and boundar_low < pivot_idx - 1:
            counter += 1
            indexes_stack.append((boundar_low, pivot_idx - 1))
        if pivot_idx < len(collection) -1 and pivot_idx + 1 < boundar_high:
            counter += 1
            indexes_stack.append((pivot_idx + 1, boundar_high))

    return counter