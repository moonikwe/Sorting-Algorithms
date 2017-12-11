#####################################################
def merge_sort(collection):
    counter = 0
    unit = 1
    while unit <= len(collection):
        h = 0
        for h in range(0, len(collection), unit * 2):
            l, r = h, min(len(collection), h + 2 * unit)
            mid = h + unit
            # merge collection[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                counter += 1
                if collection[p] < collection[q]: 
                  p += 1
                  counter += 1
                else:
                    tmp = collection[q]
                    collection[p + 1: q + 1] = collection[p:q]
                    collection[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1

        unit *= 2
    
    return counter