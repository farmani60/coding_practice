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

    def twoSum_O_n_hash(self, nums, target):
        """
        A simple implementation uses two iterations. In the first
        iteration, we add each element's value and its index to
        the table. Then, in the second iteration we check if each
        element's complement (target - nums[i]) exists in the table.

        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        map_dict = {}
        for i in range(len(nums)):
            map_dict[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in map_dict) and (map_dict[complement] != i):
                return [i, map_dict[complement]]
        return "No two sum solution!"

    def twoSum_O_n_one_pass_hash(self, nums, target):
        """
        It turns out we can do it in one-pass. While we iterate and
        inserting elements into the table, we also look back to check
        if current element's complement already exists in the table.
        If it exists, we have found a solution and return immediately.

        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        map_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map_dict:
                return [map_dict[complement], i]
            else:
                map_dict[nums[i]] = i
        return "No two sum solution!"


if __name__ == '__main__':

    twosum = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    result_O_n2 = twosum.twoSum_O_n2(nums, target)
    print("Result for the algorithm with O(n2) "
          "complexity: {}".format(result_O_n2))

    result_O_n_hash = twosum.twoSum_O_n_hash(nums, target)
    print("Result for the algorithm with O(n) "
          "complexity (hash table): {}".format(result_O_n_hash))

    result_O_n_one_pass_hash = twosum.twoSum_O_n_one_pass_hash(nums, target)
    print("Result for the algorithm with O(n) "
          "(one-pass hash table) complexity: {}".format(result_O_n_one_pass_hash))