

index = -1  # index of the found number.

def linearSearch(nums,n):
    for i in range(len(nums)):
        if nums[i] == n:
            globals()['index'] = i
            return True
    return False

sample_li = [10,2,6,8,9,5,13,11]

print(f'The sample list of numbers: {sample_li}')

num = int(input('Enter a number you want to search in the list: '))

if linearSearch(sample_li, num):
    print(f'Number found at index: {index}')
else:
    print('Number not found!')    