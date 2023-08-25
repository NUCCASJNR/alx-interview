#!/usr/bin/python3

""" This module contains a function that validates utf-8"""

from typing import List, Union


def validUTF8(data: List[int]) -> Union[bool, List[str]]:
    """
    Validates Utf-8
    """
    for char in data:
        if char in range(0, 256):
            try:
                decoded_char = bytes([char]).decode("utf-8")
            except UnicodeDecodeError:
                return False
        else:
            return False
    return True
