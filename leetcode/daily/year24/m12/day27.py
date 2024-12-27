from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = [i for i, num in enumerate(nums) if num == x]
        return [-1 if q > len(pos) else pos[q - 1] for q in queries]


if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

    # 测试数据 1：基本情况
    nums_1 = [1, 2, 3, 4, 5, 2, 3]
    queries_1 = [1, 2, 5]
    x_1 = 2
    print("Test Case 1:")
    print(solution.occurrencesOfElement(nums_1, queries_1, x_1))  # 预期输出: [1, 5, -1]

    # 测试数据 2：x 不在 nums 中
    nums_2 = [1, 3, 5, 7]
    queries_2 = [1, 2]
    x_2 = 2
    print("Test Case 2:")
    print(solution.occurrencesOfElement(nums_2, queries_2, x_2))  # 预期输出: [-1, -1]

    # 测试数据 3：所有元素都是 x
    nums_3 = [8, 8, 8, 8, 8]
    queries_3 = [1, 3, 5, 6]
    x_3 = 8
    print("Test Case 3:")
    print(solution.occurrencesOfElement(nums_3, queries_3, x_3))  # 预期输出: [0, 2, 4, -1]

    # 测试数据 4：queries 超过 x 出现次数
    nums_4 = [1, 2, 2, 2, 3]
    queries_4 = [1, 2, 3, 4]
    x_4 = 2
    print("Test Case 4:")
    print(solution.occurrencesOfElement(nums_4, queries_4, x_4))  # 预期输出: [1, 2, 3, -1]
