def math(prob:str):
    nums = prob.split()

    if nums[1] == '+':
        return int(nums[0]) + int(nums[2]) 
    
    if nums[1] == '-':
        return int(nums[0]) - int(nums[2]) 
    
    if nums[1] == '*':
        return int(nums[0]) * int(nums[2])

    if nums[1] == '//':
        if nums[2] == "0":
            return -1
        
        return int(nums[0]) // int(nums[2])
