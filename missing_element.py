"""
Nikit Parakh
Missing Element Search using Recursion
"""
import math
from typing import List


def find_missing_value(sequence: List[int]) -> int:
    """
    The function takes a list of numbers and tries to find the
    missing number in it using recursion. Time complexity is
    O[log(n)] because every recursive call splits the list in half.
    Edge cases are checked before calling inner function.
    :param sequence list of numbers from 0 to n
    :return: missing number
    """
    if not sequence:
        return 0
    if sequence[0] != 0:
        return 0
    if sequence[len(sequence) - 1] == len(sequence) - 1:
        return len(sequence)

    def find_missing_value_recursive(start: int, end: int) -> int:
        """
        This function checks if the number at the middle of start
        and end is equal to its index or not. If it is not, and the
        number before it is, then it returns it. If the previous is
        not equal to its index then the function returns itself from start
        to midpoint - 1 (left half from the middle). If the midpoint is
        equal to its index, the function returns itself from midpoint + 1 to
        end (right half from middle).
        :param start: index to start looking from
        :param end: index to end looking at
        :return: missing number or recursive call
        """
        midpoint = (start + end) // 2
        if sequence[midpoint] != midpoint:
            if sequence[midpoint - 1] == midpoint - 1:
                return midpoint
            return find_missing_value_recursive(start, midpoint - 1)
        return find_missing_value_recursive(midpoint + 1, end)
    return find_missing_value_recursive(0, len(sequence) - 1)
