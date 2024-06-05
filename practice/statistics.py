def stats(nums:'list[int]'):
    sum = 0
    min = nums[0]
    max = 0

    for int in nums:
        sum += int
        
        #max
        if int > max:
            max = int
        
        #min
        if int < min:
            min = int

    print('sum = ',sum)
    print('minimum = ',min)
    print('maximum = ',max )
    print('average = ',sum/len(nums))


test = [4,7,1,55,23,66]
stats(test)
