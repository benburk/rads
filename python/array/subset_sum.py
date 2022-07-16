"""
Given positive integers {x_1, ..., x_n}, is there a subset that sums to k

NP complete problem

Links:
    https://en.wikipedia.org/wiki/Subset_sum_problem
    https://stackoverflow.com/a/45427013/9518712
    https://cs.stackexchange.com/a/49632
    https://github.com/saltycrane/subset-sum
    https://stackoverflow.com/a/41570549/9518712
"""
from itertools import chain, combinations
from typing import Iterable

import pytest


def subset_naive(arr: list[int], k: int) -> Iterable[tuple[int, ...]]:
    """sum all subsets
    time: O(2^n)
    """
    powerset = chain.from_iterable(combinations(arr, i) for i in range(1, len(arr) + 1))
    yield from (subset for subset in powerset if sum(subset) == k)


def subset_pseudopoly(arr: list[int], k: int) -> bool:
    """
    Pseudo polynomial time using dynamic programming
    Time complexity: O(nk)
    """
    possible = [False] * (k + 1)
    possible[0] = True
    for elem in arr:
        for i in range(k - elem, -1, -1):
            if possible[i]:
                possible[i + elem] = True
    return possible[k]


# def subset_approx(arr, k, err=0.01):
#     """
#     The algorithm is polynomial time because the lists S, T and U always remain of
#     size polynomial in N and 1/c and, as long as they are of polynomial size,
#     all operations on them can be done in polynomial time.
#     """
#     s = [0]
#     for x in arr:
#         t = [x + y for y in s]
#         u = t + s
#         u = sorted(u)
#         y = u[0]  # min value of u
#         s = [y]
#         for z in u:
#             if y + err * k / len(arr) < z <= k:
#                 y = z
#                 s.append(z)
#     for x in s:
#         if (1 - err) * k <= x <= k:
#             return True
#     return False


@pytest.mark.parametrize(
    "test_input, target, expected",
    (
        ([], 1, tuple()),
        ([1], 1, True),
        ([1, 2, 3, 1], 4, True),
        ([4, 2, 3, 4], 8, True),
        ([2, 7, 9], 12, tuple()),
        ([267, 961, 1153, 1000, 1922, 493, 1598, 869, 1766, 1246], 5842, True),
    ),
)
def test(test_input: list[int], target: int, expected: list[tuple[int, ...]]) -> None:
    """Run test cases.

    :param test_input: The input to the function.
    :param expected: The expected output.
    """

    assert subset_naive(test_input, target) == expected
    # assert subset_pseudopoly(test_input, target) == expected
    # assert subset_approx(test_input, target) == expected
