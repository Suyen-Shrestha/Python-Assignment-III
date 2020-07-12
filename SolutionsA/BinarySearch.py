
index = -1 # index for the found number.

def binarySearch(nums,n):
    low = 0     #lower bound
    upp = len(nums) - 1 #upper bound

    while low < upp:
        mid = (low + upp) // 2
        if nums[mid] == n:
            globals()['index'] = mid
            return True
        elif nums[mid] < n:
            low = mid + 1          
        else:
            upp = mid - 1



sample_li = [12,8,7,9,10,14,25,66,80,100]
sample_li.sort() #array needs to be sorted in binary search.
print(f'The sample list of numbers: {sample_li}')
num = int(input('Enter a number you want to search in the list: '))

if binarySearch(sample_li,num):
    print(f'Number found at index: {index}')
else:
    print('Number not found!')    


