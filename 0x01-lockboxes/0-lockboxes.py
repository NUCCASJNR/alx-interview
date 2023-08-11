#!/usr/bin/python3
"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""
def canUnlockAll(boxes):
    unlocked_boxes = [0]  # Start with box 0, which is initially unlocked
    index = 0

    while index < len(unlocked_boxes):
        box_keys = boxes[unlocked_boxes[index]]
        # print(box_keys)
        for key in box_keys:
            print(key)
            if key not in unlocked_boxes:
                unlocked_boxes.append(key)

        index += 1

    return len(unlocked_boxes) == len(boxes)

# Example usage
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
