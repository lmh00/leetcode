def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        print("_" * 20)
        print(i, n)
        diff = target - n
        print(diff)
        print(prevMap)
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
        print(prevMap)
        print("_" * 20)

twoSum([1, 2, 3, 4, 5], 9)
