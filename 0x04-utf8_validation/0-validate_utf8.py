#!/usr/bin/python3

""" This module contains a function that validates utf-8"""

from typing import List, Union


# def validUTF8(data: List[int]) -> Union[bool, List[str]]:
#     """
#     Validates Utf-8
#     """
#     for char in data:
#         if char in range(0, 256):
#             try:
#                 decoded_char = bytes([char]).decode("utf-8")
#             except IndexError and UnicodeError:
#                 return False
#         else:
#             return False
#     return True

def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
    :param data:
    """
    num_bytes = 0
    for byte in data:
        mask = 1 << 7
        if not num_bytes:
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0
