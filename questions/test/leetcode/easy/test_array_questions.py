from questions.leetcode.easy import array_questions
import unittest


class ArrayQuestionsTest(unittest.TestCase):
    arr = array_questions.ArrayQuestions()

    # Problem : Remove Duplicates from Sorted Array
    def test_remove_duplicates_empty(self):
        nums = []
        self.assertEqual(self.arr.remove_duplicates(nums), 0)
        self.assertEqual(nums, [])

    def test_remove_duplicates(self):
        nums = [1, 1, 1, 2, 3, 3, 4]
        self.assertEqual(self.arr.remove_duplicates(nums), 4)
        self.assertEqual(nums[:4], [1, 2, 3, 4])

    # Problem : Best Time to Buy and Sell Stock II
    def test_max_profit(self):
        prices = [1, 1, 2, 4, 0, 1, 2]
        self.assertEqual(self.arr.max_profit(prices), 5)

    def test_max_profit_empty(self):
        prices = []
        self.assertEqual(self.arr.max_profit(prices), 0)

    def test_max_profit_no_profit(self):
        prices = [5, 4, 2, 1]
        self.assertEqual(self.arr.max_profit(prices), 0)

    # Problem : Rotate Array
    def test_rotate_array_right(self):
        nums = [1, 2, 3, 4, 5]
        self.arr.rotate_array(nums, 2)
        self.assertEqual(nums, [4, 5, 1, 2, 3])

    def test_rotate_array_left(self):
        nums = [1, 2, 3, 4, 5]
        self.arr.rotate_array(nums, -4)
        self.assertEqual(nums, [5, 1, 2, 3, 4])

    def test_rotate_array_large(self):
        nums = [1, 2, 3, 4, 5]
        self.arr.rotate_array(nums, 21)
        self.assertEqual(nums, [5, 1, 2, 3, 4])

    # Problem : Contains Duplicate
    def test_contains_duplicate_false(self):
        nums = [1, 2, 3]
        self.assertFalse(self.arr.contains_duplicate(nums))

    def test_contains_duplicate_true(self):
        nums = [1, 1, 2]
        self.assertTrue(self.arr.contains_duplicate(nums))

    def test_contains_duplicate_empty(self):
        nums = []
        self.assertFalse(self.arr.contains_duplicate(nums))

    # Problem : Single Number
    def test_single_number_set(self):
        nums = [1, 2, 2, 3, 1]
        self.assertEqual(self.arr.single_number_set(nums), 3)

    def test_single_number_sort(self):
        nums = [1, 2, 2, 3, 1]
        self.assertEqual(self.arr.single_number_sort(nums), 3)

    def test_single_number_bit(self):
        nums = [1, 2, 2, 3, 1]
        self.assertEqual(self.arr.single_number_bit(nums), 3)

    # Problem : Move Zeroes
    def test_move_zeroes(self):
        nums = [1, 0, 1, 0, 3, 12]
        self.arr.move_zeroes(nums)
        self.assertEqual(nums, [1, 1, 3, 12, 0, 0])