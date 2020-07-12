

def partition(nums, start, end):
    pivot = nums[end] # selecting the last element in the list as pivot element.
    pIndex = start # selecting the start index as partition Index.

    for i in range(start,end):
        if (nums[i] <= pivot):
            nums[i], nums[pIndex] = nums[pIndex], nums[i]
            pIndex += 1

    nums[pIndex], nums[end] = nums[end], nums[pIndex]
    return pIndex 



def quickSort(nums, start, end):
    if start < end:
        partition_index = partition(nums, start, end)

        quickSort(nums, start, partition_index-1) # sorting elements lesser than pivot
        quickSort(nums, partition_index+1, end) # sorting elements greater than pivot





arr = input('Enter a list of numbers separated by comma: ').split(',')
sample_nums = [int(x.strip()) for x in arr] 

n = len(sample_nums)

quickSort(sample_nums,0,n-1) 
print(f'The array list after quick sort: {sample_nums}')