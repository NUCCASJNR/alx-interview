#!/usr/bin/python3

"""Making change"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """

    Args:
        coins: list of coins
        total: Amount to be met
    Returns:
        Fewest Number
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    total_coins_used = 0
    for coin in sorted_coins:
        while total >= coin:
            total -= coin
            total_coins_used += 1
    if total == 0:
        return total_coins_used
    return -1
