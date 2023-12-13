def sort(nums):
    for i in range(len(nums)-1): #bubbling up
        is_swapped = False
        for j in range(len(nums)-i-1): #no. of comparisons 5-0-1 = 4
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True

        if not is_swapped:
            break
    return nums

nums = [7, 4, 3, 5, 1]
sort(nums)
print(nums)