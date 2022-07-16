"""Find three values that sum to a target.

https://leetcode.com/problems/3sum/
https://en.wikipedia.org/wiki/3SUM
"""

from typing import Iterator, Sequence

import pytest


def three_sum_naive(
    arr: Sequence[int], target: int = 0
) -> Iterator[tuple[int, int, int]]:
    """Return triples of indices that sum to target.
    time: O(n^3)
    space: O(1)

    :param arr: array of ints
    :param target: target sum
    :return: iterator of tuples of indices
    """
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    yield i, j, k


def three_sum_closest(nums: list[int], target: int) -> int:
    """Return total closest to target.

    time: O(n^2)
    """
    nums = sorted(nums)
    result = sum(nums[:3])  # initial sum
    for i, _ in enumerate(nums):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < abs(result - target):
                result = total

            if total < target:  # move left pointer rightward for larger val
                left += 1
            elif total > target:  # move right pointer leftward for smaller val
                right -= 1
            else:  # if total == target, we can directly return
                return result
    return result


def three_sum(arr: list[int]) -> set[tuple[int, int, int]]:
    """O(n^2)
    Compact, but slow on arrays with many duplicates
    """
    result = set()
    arr = sorted(arr)

    for i in range(len(arr) - 2):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            if arr[i] + arr[start] + arr[end] == 0:
                result.add((arr[i], arr[start], arr[end]))
            if arr[i] + arr[start] + arr[end] < 0:
                start += 1
            else:
                end -= 1

    return result


def three_sum_fast(arr: list[int]) -> Iterator[tuple[int, int, int]]:
    """O(n^2)"""
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        start = i + 1
        end = len(arr) - 1

        while start < end:
            if arr[i] + arr[start] + arr[end] == 0:
                yield i, start, end
            if arr[i] + arr[start] + arr[end] < 0:
                current_start = start
                while arr[start] == arr[current_start] and start < end:
                    start += 1
            else:
                current_end = end
                while arr[end] == arr[current_end] and start < end:
                    end -= 1


@pytest.mark.parametrize(
    "array, target, expected",
    (
        ([], 0, []),
        ([0, 0, 0], 0, [0, 0, 0]),
        ([-1, 0, 1, 2, -1, -4], 0, [(-1, 0, 1), (-1, -1, 2)]),
    ),
)
def test(array: list[int], target: int, expected: list[tuple[int, int, int]]) -> None:
    """run test cases
    Test cases just use 0 as target
    """
    # assert len(three_sum(test_input)) == expected
    # assert len(three_sum_fast(test_input)) == expected
    assert list(three_sum_naive(array, target)) == expected
