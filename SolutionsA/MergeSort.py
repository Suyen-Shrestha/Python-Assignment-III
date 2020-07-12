

def merge(arr, left, right):
    i = 0   #index of smallest unpicked value in left array.
    j = 0   #index of smallest unpicked value in right array.
    k = 0   #index of original array where value needs to be positioned .

    while (i < len(left)) and (j < len(right)):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1 

    while (i < len(left)):
        arr[k] = left[i]
        k += 1
        i +=1

    while (j < len(right)):
        arr[k] = right[j]
        k += 1
        j += 1  


def mergeSort(arr):

    # sort only if array contains more than one element.
    if len(arr) > 1:
        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # sort left and right halves of the array separately
        mergeSort(left_arr)        
        mergeSort(right_arr)
        merge(arr, left_arr, right_arr)             



arr = input('Enter a list of numbers separated by comma: ').split(',')
sample_arr = [int(x.strip()) for x in arr] 

mergeSort(sample_arr)
print(f'The final array after merge sort: {sample_arr}')