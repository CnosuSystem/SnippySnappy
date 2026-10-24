# Copyright Cnosu System 2026. GPLv3 license, see the LICENSE.md file.

# Test if the functions in ids.py actually work.

# Check bubble_sort.

from snippysnappy import bubble_sort


def test_bubble_sort_1():
    assert bubble_sort([3, 2, 4, 18]) == [2, 3, 4, 18]


def test_bubble_sort_2():
    assert bubble_sort([9, 7, 6, 256, 128, 1892, 728]) == [6, 7, 9, 128, 256, 728, 1892]


def test_bubble_sort_3():
    assert bubble_sort([3.5, 1.2, 4.8, 2.1, 0.5]) == [0.5, 1.2, 2.1, 3.5, 4.8]


# Check optimized_bubble_sort.

from snippysnappy import optimized_bubble_sort


def test_optimized_bubble_sort_1():
    assert optimized_bubble_sort([3, 2, 4, 18]) == [2, 3, 4, 18]


def test_optimized_bubble_sort_2():
    assert optimized_bubble_sort([9, 7, 6, 256, 128, 1892, 728]) == [
        6,
        7,
        9,
        128,
        256,
        728,
        1892,
    ]


def test_optimized_bubble_sort_3():
    assert optimized_bubble_sort([3.5, 1.2, 4.8, 2.1, 0.5]) == [0.5, 1.2, 2.1, 3.5, 4.8]
