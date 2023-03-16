        x = 0
        l = len(nums)-1
        while x <= l:
            mid =  x + (l-x)//2
            if nums[mid] == target:
                    return mid
            if nums[mid] < target:
                    x =  mid + 1
            else:
                    l =  mid - 1
        return -1
