class EasyArray():

    # Problem : Remove Duplicates from Sorted Array
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def remove_duplicates(self, nums):
        if (len(nums) < 2):
            return len(nums)

        i = 0
        for j in range(1, len(nums)):
            if (nums[i] < nums[j]):
                temp = nums[j]
                nums[j] = nums[i + 1]
                nums[i + 1] = temp
                i += 1
        return i + 1

    # Problem : Best Time to Buy and Sell Stock II
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def max_profit(self, prices):
        if (len(prices) < 2):
            return 0

        profit = []
        profit.append(0)

        for i in range(1, len(prices)):
            if prices[i] <= prices[i - 1]:
                profit.append(profit[i - 1])
            else:
                profit.append(profit[i - 1] + (prices[i] - prices[i - 1]))
        return profit[-1]

    # Problem : Rotate Array
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def rotate_array(self, nums, k):
        k = k % len(nums)

        l = []
        i = -k
        while (i < len(nums) - k):
            l.append(nums[i])
            i += 1

        for i in range(0, len(nums)):
            nums[i] = l[i]

    # Problem : Contains Duplicate
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def contains_duplicate(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False

    # Problem : Single Number
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def single_number_set(self, nums):
        num_set = set()
        for i in nums:
            if i in num_set:
                num_set.remove(i)
            else:
                num_set.add(i)
        return num_set.pop()

    # Problem : Single Number
    # Time Complexity : O(n log n)
    # Space Complexity : O(1)
    def single_number_sort(self, nums):
        nums.sort()
        for i in range(0, len(nums), 2):
            if (i + 1 == len(nums)) or (nums[i] != nums[i + 1]):
                return nums[i]

    # Problem : Single Number
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def single_number_bit(self, nums):
        xor = 0
        for i in nums:
            xor = xor ^ i
        return xor

    # Problem : Move Zeroes (283)
    # * In-place
    # * Minimize total number of operations
    # Time Complexity : O(n^2)
    # Space Complexity : O(1)
    def move_zeroes_brute_force(self, nums):
        i = 0
        j = 1
        while (i < len(nums) and j < len(nums)):
            if (nums[i] == 0) and (nums[j] != 0):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j = i + 1
            elif (nums[i] == 0) and (nums[j] == 0):
                j += 1
            else:
                i += 1
                j += 1

    # Problem : Move Zeroes (283)
    # * In-place
    # * Minimize total number of operations
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def move_zeroes(self, nums):
        zero_index = 0
        for i in nums:
            if (i != 0):
                nums[zero_index] = i
                zero_index += 1
        for i in range(zero_index, len(nums)):
            nums[i] = 0