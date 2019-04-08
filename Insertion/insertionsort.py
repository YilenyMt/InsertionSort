def insertion_sort(list):
    print("Array values: ", list)
    for i in range(1,len(list)):
        ix = i
        while(ix!=0 and list[ix] < list[ix-1]):
            list[ix-1], list[ix] = list[ix], list[ix-1]
            ix-=1
    print("sorted list insertion: ", list)
    return list

values = [2,8,6,1,4]
insertion_sort(values)