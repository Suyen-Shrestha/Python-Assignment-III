

def bubbleSort(nums):
    for n in range(1,len(nums)):
        for i in range(len(nums)- n):
            if (nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i+1], nums[i]
    return nums             


input_nums = input('Enter a list of numbers separated by comma: ').split(',')
sample_nums = [int(i.strip()) for i in input_nums]

print(f'The output after bubble sort: {bubbleSort(sample_nums)}')


