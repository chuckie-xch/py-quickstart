from itertools import pairwise
import unittest


class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(a.lower() != b.lower() for a, b in pairwise(s))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countKeyChanges_EmptyString_ShouldReturnZero(self):
        self.assertEqual(self.sol.countKeyChanges(""), 0)

    def test_countKeyChanges_SingleCharacter_ShouldReturnZero(self):
        self.assertEqual(self.sol.countKeyChanges("a"), 0)

    def test_countKeyChanges_AllSameCase_ShouldReturnZero(self):
        self.assertEqual(self.sol.countKeyChanges("abcdef"), 5)


    def test_countKeyChanges_ConsecutiveSame_ShouldReturnZero(self):
        self.assertEqual(self.sol.countKeyChanges("aa"), 0)

    def test_countKeyChanges_ConsecutiveDifferent_ShouldReturnOne(self):
        self.assertEqual(self.sol.countKeyChanges("aB"), 1)


if __name__ == '__main__':
    unittest.main()
