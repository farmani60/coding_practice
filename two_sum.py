# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

import time


class Solution(object):

    def twoSum_O_n(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target-nums[i]] = i
        return "No two sum solution!"

    def twoSum_O_n2(self, nums, target):
        """
        Brute force approach. Loop through each element x and
        find if there is another value that equals to target - x.

        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return "No two sum solution!"


if __name__ == '__main__':

    twosum = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    result_O_n = twosum.twoSum_O_n(nums, target)
    print("Result for the algorithm with O(n) "
          "complexity: {}".format(result_O_n))

    result_O_n2 = twosum.twoSum_O_n2(nums, target)
    print("Result for the algorithm with O(n2) "
          "complexity: {}".format(result_O_n2))