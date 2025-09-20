"""Simple implementation of the bubble sort algorithm."""
from __future__ import annotations

from typing import Iterable, List, MutableSequence, TypeVar

T = TypeVar("T")


def bubble_sort(values: Iterable[T]) -> List[T]:
    """Return a new list containing ``values`` sorted in ascending order.

    The implementation uses the classic bubble sort algorithm, which
    repeatedly swaps adjacent elements that are out of order until the list
    is sorted. While bubble sort is not efficient for large datasets, it is
    easy to implement and useful for educational purposes.
    """

    items: MutableSequence[T] = list(values)
    n = len(items)
    if n < 2:
        return list(items)

    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return list(items)


if __name__ == "__main__":
    data = [5, 1, 4, 2, 8]
    print("Original:", data)
    print("Sorted:", bubble_sort(data))
