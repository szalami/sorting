nums = [87, 23, 44, 100, 0, 12, 1, 65, 43, 51, 99, 74]


temp = 0
lenght = len(nums)
for i in range(lenght):
    for j in range(0, lenght-i-1):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            
            
print(nums)
            
                    