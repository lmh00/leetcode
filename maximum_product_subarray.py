def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

maxProduct([1, 2, -3, 4])
