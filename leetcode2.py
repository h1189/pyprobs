class Solution:
    def twoSum(self, nums, target: int):  
        res = 0
        output = []
        for i in range (0,len(nums)):
            for j in range (0, len(nums)):
                res = nums[i] + nums[j]
                if res == target:
                    a = nums.index(nums[i])
                    print(a)
                    b = nums.index(nums[j])
                    print(b)
                    output.append(a)
                    output.append(b)
                    print(f'target matched {res}')
                    return output
                    

nums = [3, 9, 3]
target = 12
k = Solution().twoSum(nums, target)
print(k)    