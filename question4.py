def findMaxLength(nums):
    count_dict = {0: -1}  # Initialize with count 0 at index -1
    count = 0
    max_len = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in count_dict:
            curr_len = i - count_dict[count]
            max_len = max(max_len, curr_len)
        else:
            count_dict[count] = i

    return max_len
nums = [0, 1]
print(findMaxLength(nums))
