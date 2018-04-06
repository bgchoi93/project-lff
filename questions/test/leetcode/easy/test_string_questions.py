from questions.leetcode.easy import string_questions
import unittest

class StringQuestionsTest(unittest.TestCase):

    str = string_questions.StringQuestions()

    # Problem : Reverse String

    def test_reverse_string_stack(self):
        s = "abcd"
        self.assertEqual(self.str.reverse_string_stack(s), "dcba")

    def test_reverse_string_list(self):
        s = "abcd"
        self.assertEqual(self.str.reverse_string_list(s), "dcba")