

def insertionSort(nums):
    for i in range(len(nums)):
        value = nums[i]
        holeIndex = i
        while (holeIndex > 0) and (nums[holeIndex - 1] > value):
            nums[holeIndex] = nums[holeIndex - 1]
            holeIndex = holeIndex - 1

        nums[holeIndex] = value
        
    return nums


input_nums = input('Enter a list of numbers separated by comma: ').split(',')
sample_nums = [int(i.strip()) for i in input_nums]

print(f'The output after insertion sort: {insertionSort(sample_nums)}')         