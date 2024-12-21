class Solution:
    def productExceptSelf(self, nums):
        arr = [0] * len(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            arr[i] = product
        return arr