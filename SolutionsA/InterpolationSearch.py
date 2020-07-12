

def interpolationSearch(nums,n):
    low = 0  #upper bound
    upp = len(nums) - 1  #lower bound

    while (low <= upp):
        mid = low + ((n - nums[low])*(upp-low)) // (nums[upp] - nums[low]) #interpolation formula for calculating mid value in array.

        if nums[mid] == n:
            return mid

        elif nums[mid] < n:
            low = mid + 1
        else:
            high = mid - 1  

    return -1  



sample_arr = [22, 23, 24, 33, 35, 42, 47, 13, 16, 18, 19, 20, 21]
sample_arr.sort()

print(f'The sample list of numbers: {sample_arr}')
num = int(input('Enter a number you want to search on the list: '))

pos = interpolationSearch(sample_arr,num)

if pos != -1:
    print(f'Number found at postion: {pos}')
else:
    print('Number not found!')    