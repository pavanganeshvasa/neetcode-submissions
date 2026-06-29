class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        firstzero = False
        secondzero = False
        prod = 1

        for n in nums:
            if(n == 0):
                if(not firstzero):
                    firstzero = True
                    continue
                else:
                    secondzero = True
                    continue
            prod = prod * n
        
        if(secondzero):
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            if(firstzero and not secondzero and nums[i] != 0):
                res[i] = 0
            elif(nums[i] != 0):
                res[i] = int(prod/nums[i])
            else:
                res[i] = prod
            

        return res

