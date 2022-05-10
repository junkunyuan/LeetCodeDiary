class Solution_1:
    """ Solution 1
        O(n^2);
        time: 5968ms, memory: 15.1MB;
        ind_1: for loop of nums;
        ind_2: for loop of nums, ind_2 == target - ind_1.
    """
    def twoSum(self, nums, target):
        for ind_1 in range(len(nums)):
            for ind_2 in range(len(nums)):
                if nums[ind_1] + nums[ind_2] == target and ind_1 != ind_2:
                    return [ind_1, ind_2]


class Solution_2:
    """ Solution 2 (my solution)
        O(n);
        time: 372ms; memory: 15.1MB;
        ind_1: for loop of nums;
        ind_2: the first element of nums[ind_1 + 1:] == target - nums[ind_1]
    """
    def twoSum(self, nums, target):
        for ind_1 in range(len(nums)):
            diff = target - nums[ind_1]
            if diff in nums[ind_1 + 1:]:
                ind_2 = nums[ind_1 + 1:].index(diff) + ind_1 + 1
                return [ind_1, ind_2]


class Solution_3:
    """ Solution 3 (https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/) 
        O(n);
        time: 44ms; memory: 15.8MB;
        ind_1: hash map of nums;
        ind_2: search the hash map.
    """
    def twoSum(self, nums, target):
        hashmap = {}
        for ind_2, num_2 in enumerate(nums):
            hashmap[num_2] = ind_2
        for ind_1, num_1 in enumerate(nums):
            ind_2 = hashmap.get(target - num_1)
            if ind_2 is not None and ind_1 != ind_2:
                return [ind_1, ind_2]
