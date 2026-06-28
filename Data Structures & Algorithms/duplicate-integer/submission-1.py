class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set()
        for i in range(len(nums)):
            if nums[i] in nums1:
                return True
            nums1.add(nums[i])

        return False


        